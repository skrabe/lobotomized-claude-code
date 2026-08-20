<!--
name: 'Data: Managed Agents multiagent sessions'
description: >-
  Reference documentation for Managed Agents multiagent sessions, including
  coordinator rosters, threads, session stream events, subagent tool
  permissions, and pitfalls
ccVersion: 2.1.237
-->
# Managed Agents — Multiagent Sessions

A coordinator agent can delegate to other agents within one session. All agents **share the container and filesystem**; each runs in its own **thread** — a context-isolated event stream with its own conversation history, model, system prompt, tools, MCP servers, and skills (from that agent's own config). Threads are persistent: the coordinator can send a follow-up to a subagent it called earlier and that subagent retains its prior turns.

The SDK sets the `managed-agents-2026-04-01` beta header automatically on all `client.beta.{agents,sessions}.*` calls; no additional header is required for multiagent.

Delegate when the work splits into independent pieces, or when one piece would fill the coordinator's context with reading. Each delegated piece runs in its own thread with a fresh context window, threads run in parallel in the same container, and only each subagent's report comes back. There is no orchestration code to write: the coordinator is given delegation tools automatically, and the client still creates one session and reads one stream. A small single-step task is a poor fit — every delegation costs a round-trip and a re-briefing.

Platform guide: `https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration.md`.

---

## Declare the roster on the coordinator

`multiagent` is a **top-level field** on `agents.create()` / `agents.update()` — **not** a `tools[]` entry. `agents` lists 1–20 roster entries. Nothing changes on `sessions.create()` — the roster is resolved from the coordinator's config.

```python
orchestrator = client.beta.agents.create(
    name="Engineering lead",
    model="{{OPUS_ID}}",
    system="You coordinate engineering work. Delegate code review to the reviewer and test writing to the test agent.",
    tools=[{"type": "agent_toolset_20260401"}],
    multiagent={
        "type": "coordinator",
        "agents": [
            reviewer.id,                                            # bare string — latest version
            {"type": "agent", "id": test_writer.id, "version": 4},  # pinned version
            {"type": "self"},                                       # the coordinator itself
        ],
    },
)
```

| Roster entry | Shape | Notes |
|---|---|---|
| String shorthand | `"agent_abc123"` | References the latest version of a stored agent. |
| Agent reference | `{type: "agent", id, version?}` | Omit `version` to pin the latest at coordinator save time. |
| Self | `{type: "self"}` | The coordinator can spawn copies of itself. |
| Advisor | `{type: "advisor", model}` | A model the session's primary thread can consult mid-turn. At most one per roster. See § Advisor below. |

A roster entry is only a reference: a worker runs on its own `model`, `system`, and `tools`, and its tokens are billed at its own model's rates. If the session was created with `agent_with_overrides`, those overrides apply to the **coordinator and its `self` copies** — roster agents referenced by ID always use their own as-created configuration.

The coordinator's thread receives delegation tools for working the roster: `list_agents` (see the roster) and `send_to_agent` (task or message a member). It chooses whom to spawn from each entry's `name` and `description` (the `self` entry is listed under the coordinator's own name), so write both for the coordinator to read. Names must be unique across the roster; don't name an agent `self`. Subagents see none of the coordinator's conversation, so each task must carry the paths, constraints, and report format it needs. Spawning returns immediately; the subagent's report arrives in a later coordinator turn.

**Web tool domain lists layer, never widen.** A roster agent's `web_search` / `web_fetch` calls are bound by its own `allowed_domains` / `blocked_domains`, by those of every agent that called it, and by the coordinator's current lists (allow-lists intersect, block-lists union). Keep each roster agent's allow-list inside the coordinator's — disjoint lists leave the tool present but every call fails `url_not_allowed`.

**Limits:** 1–20 roster entries (at most one `self`; each rostered agent can be spawned many times), **one level of delegation** — enforced, not silently flattened: rostering an agent that itself carries a `multiagent.agents` roster fails the create or update with a validation error — and at most **25 concurrent threads** per session; archive finished threads if a long session needs more.

**Inference geo pins must be roster-uniform.** When agents pin an inference geography (`model.inference_geo`), the coordinator's pin and every roster member's must all be the same value or all be unset. A mismatched roster is a 400 validation error, both when the agent is saved and when a session-create `model` override changes any of the pins.

---

## Threads

The session-level event stream is the **primary thread** — it shows the coordinator's trace plus a condensed view of subagent activity (thread status transitions and cross-thread messages, not every subagent tool call). Drill into a specific subagent via the per-thread endpoints:

| Operation | HTTP | SDK (`client.beta.sessions.threads.*`) |
|---|---|---|
| List threads | `GET /v1/sessions/{sid}/threads` | `.list(session_id)` |
| Retrieve one | `GET /v1/sessions/{sid}/threads/{tid}` | `.retrieve(thread_id, session_id=...)` |
| Archive | `POST /v1/sessions/{sid}/threads/{tid}/archive` | `.archive(thread_id, session_id=...)` |
| List thread events | `GET /v1/sessions/{sid}/threads/{tid}/events` | `.events.list(thread_id, session_id=...)` |
| Stream thread events | `GET /v1/sessions/{sid}/threads/{tid}/stream` | `.events.stream(thread_id, session_id=...)` |

Each `SessionThread` carries `id`, `status` (`running` | `idle` | `rescheduling` | `terminated`), `agent` (a resolved snapshot of the agent config — `id`, `name`, `model`, `system`, `tools`, `skills`, `mcp_servers`, `version` — except advisor threads, whose `agent` is the two-field advisor form `{"type": "advisor", "model": ...}`), `parent_thread_id` (null for the primary thread, which is included in the list), `archived_at`, and optional `stats`/`usage`. Per-thread `usage.list_cost` figures do **not** sum to the session total — the session figure additionally includes session running time and each figure is rounded independently; the session-level `usage.list_cost` is authoritative. **Session status aggregates thread statuses** — if any thread is `running`, `session.status` is `running`. Max **25 concurrent threads** (advisor threads are exempt). When draining a per-thread stream, break on `session.thread_status_idle` (and check its `stop_reason` as you would for the session-level idle).

**A session budget is one shared cap across all threads** — no per-thread caps. Each thread's consumption is priced at its own served model, and threads pause independently (`stop_reason: budget_reached`) as the shared cap is reached; one thread can pause while another finishes its in-flight request. A thread waiting on `requires_action` outranks the cap at the session level.

---

## Multiagent events (on the session stream)

| Event | Payload highlights | Meaning |
|---|---|---|
| `session.thread_created` | `session_thread_id`, `agent_name` | A new thread was created. |
| `session.thread_status_running` | `session_thread_id`, `agent_name` | Thread started activity. |
| `session.thread_status_idle` | `session_thread_id`, `agent_name`, **`stop_reason`** | Thread is awaiting input — or paused at the session's shared budget (`stop_reason: budget_reached`). Inspect `stop_reason` (same shape as `session.status_idle.stop_reason`). |
| `session.thread_status_rescheduled` | `session_thread_id`, `agent_name` | Thread is rescheduling after a retryable error. |
| `session.thread_status_terminated` | `session_thread_id`, `agent_name` | Thread ended — completed its work and self-terminated (advisor consultation threads), was archived, or hit a terminal error. |
| `agent.thread_message_sent` | `to_session_thread_id`, `to_agent_name`, `content` | *This* thread sent a message to another thread. On the primary stream: the coordinator sent a task or follow-up to an agent. |
| `agent.thread_message_received` | `from_session_thread_id`, `from_agent_name`, `content` | A message arrived on *this* thread from another. On the primary stream: an agent sent a report or question to the coordinator. |

> **Direction is relative to the thread whose stream carries the event**, not to the coordinator. The same delegated task is an `agent.thread_message_sent` on the primary stream and an `agent.thread_message_received` on the child's own stream. Reading `_received` as "a subagent finished" is wrong once you're reading a child stream.

**Previewing a subagent's text.** Each thread's stream accepts the same `event_deltas[]` parameter as the session-level stream (`GET /v1/sessions/{sid}/threads/{tid}/stream?event_deltas%5B%5D=agent.message`). **Previews are thread-scoped** — a child's previews are delivered only on that child's stream and never cross-posted to the session-level stream, so watching a subagent live means opening its thread stream. **Only plain assistant text previews:** a subagent's *reply to its coordinator* rides `agent.thread_message_sent` and is never previewed, so a worker that does nothing but report back streams no deltas at all even with a correct opt-in on the right thread. To get a live preview out of a subagent, its prompt has to make it write the answer as a plain assistant message in its own thread first, and only then report to the coordinator.

---

## Advisor

An `{"type": "advisor", "model": "<model id>"}` roster entry gives the session's **primary thread** an advisor: a model it can consult mid-turn for strategic guidance. The entry has exactly two fields — `type` and `model` — and can sit alongside any other roster forms; a roster with no other entries works too. The advisor is also available as a server tool on the Messages API (`advisor_20260301`); the Managed Agents surface differs in configuration and delivery: the roster entry has **no `max_uses`, `max_tokens`, or `caching` fields**, and advice arrives through thread events rather than `advisor_tool_result` blocks.

({{OPUS_NAME}} is the default advisor choice. It is a redacted advisor — the agent reads its advice server-side, but the client sees `[{"type": "redacted"}]`. For client-readable advice, a plaintext advisor such as `claude-opus-4-8` is valid only when the agent's own model is `claude-opus-4-8` or below — agents on {{OPUS_NAME}}, {{FABLE_NAME}}, or {{MYTHOS_NAME}} can only pair with redacted advisors, so client-readable advice is not available for them.)

**Rules:**
- **At most one advisor entry per roster.** The entry occupies the reserved roster name `anthropic.advisor` — a roster that also lists a member literally named `anthropic.advisor` is a 400. In responses, the advisor entry is echoed **last** in the roster regardless of submitted position.
- **Pairing is validated at agent save:** the advisor model must meet a minimum capability bar, and the agent's own model must not be more capable than its advisor (equals can pair). Invalid pairing → 400.
- **Only the primary thread consults it.** The advisor is not a roster agent: invisible to the coordinator's `list_agents` tool, unreachable via `send_to_agent`, and roster agents cannot consult it.

**How consultations work.** Each consultation runs as a platform-spawned thread named `anthropic.advisor` that terminates itself when done; the advice is delivered to the primary thread as an `agent.thread_message_received` event. Typical event order (the reserved name rides `agent_name` on lifecycle events and `from_agent_name` on the delivery): `session.thread_created` → `session.thread_status_running` → `agent.thread_message_received` (the advice) → `session.thread_status_idle` (`stop_reason: end_turn`) → `session.thread_status_terminated`. No `agent.tool_use` and no `agent.thread_message_sent` are emitted for a consultation, and **the advice delivery is not guaranteed to precede the advisor thread's idle/terminated events** — don't treat those as "advice already delivered."

**Plaintext vs redacted delivery.** Whether the client can read the advice is the advisor model's policy: models that return plaintext there deliver readable text content here; models that return redacted results deliver `[{"type": "redacted"}]` as the message content on every client surface, while the agent still reads the full advice server-side. Advisor thinking is never surfaced. Clients cannot send `redacted` blocks themselves — an event containing one is a 400.

**Failure and interruption.** A failed consultation — or one abandoned via a `user.interrupt` carrying the advisor thread's `session_thread_id` — never fails the agent's turn: the agent continues after a generic notice. A session-level `user.interrupt` during a consultation halts the whole session as usual, terminating the advisor thread with no advice delivered.

**Threads, billing, caching.** Advisor threads are **exempt from the 25-concurrent-thread limit**. They appear in the session's thread list with `agent` set to the advisor form as configured and `parent_thread_id` set to the primary thread. Consultations are billed at the advisor model's rates. Advisor-side prompt caching is automatic.

**Removing the advisor:** update the agent with a roster that omits the entry; if the advisor is the roster's only entry, clear the roster with `"multiagent": null`.

---

## Tool permissions from subagent threads

When a subagent needs the client (an `always_ask` confirmation, or a custom tool result), the request is **cross-posted to the primary thread** with `session_thread_id` identifying the originating thread — so only the session stream needs watching. Reply with `user.tool_confirmation` (carrying `tool_use_id`) or `user.custom_tool_result` (carrying `custom_tool_use_id`), and **echo the `session_thread_id` from the originating event**. The server also routes by the tool-use ID, so the echo is belt-and-suspenders rather than load-bearing — but include it.

## Interrupting and archiving threads

- **`user.interrupt` without `session_thread_id` interrupts every non-archived thread in the session, including the primary** — it is not a primary-only stop. Pass `session_thread_id` to target one thread.
- **Against a child thread blocked on `requires_action`**, the interrupt closes each pending tool call with an *error* tool result (`"Tool execution was interrupted before completion. Please retry."`) and re-emits `session.thread_status_idle` with `stop_reason: end_turn` directly — the model is not sampled. Against a thread already `idle`, the interrupt is a no-op — with one exception: a session on a self-hosted environment whose worker failed the claimed work item (e.g. a memory-store mount error) sits `idle`, and a `user.interrupt` re-queues that work so the next worker claim retries (`shared/managed-agents-self-hosted-sandboxes.md` § Memory stores → Troubleshooting).
- **Archive requires the thread to be idle, and `requires_action` counts as idle** — a thread parked on a pending tool call can be archived directly. Only a *running* thread must be interrupted first.

## Pitfalls

- **Don't put the roster on `sessions.create()` or in `tools[]`.** `multiagent` is a top-level agent field; update the coordinator, then start a session that references it.
- **Don't assume shared context.** Threads share the filesystem but not conversation history or tools. If the coordinator needs a subagent to act on something, it must say so in the delegated message (or write it to disk).
- **Depth > 1 is a validation error.** Rostering an agent that itself carries a `multiagent.agents` roster fails the create or update — only the session's coordinator delegates.
