<!--
name: 'Data: Managed Agents client patterns'
description: >-
  Reference guide of common client-side patterns for driving Managed Agent
  sessions, including stream reconnection, idle-break gating, tool
  confirmations, interrupts, and custom tools
ccVersion: 2.1.237
-->
# Managed Agents — Common Client Patterns

## 1. Lossless stream reconnect

Tail the live stream. Dedupe only gates handle() — terminal checks must run even for already-seen events, or a terminal event that was in the history response gets skipped by `continue` and the loop never exits.

---

## 2. `processed_at` — queued vs processed

Every event on the stream carries `processed_at` (ISO 8601), set when the event finishes processing. For client-sent events (`user.message`, `user.interrupt`, `user.tool_confirmation`) it's `null` while the event is queued behind earlier ones, and populated once the agent processes it — so the same event appears on the stream twice, once with `null` and once with a timestamp. (Exception: a `user.interrupt` sent while the session is paused at its budget is accepted and ignored — it never appears at all; see `shared/managed-agents-events.md` § Reaching a session budget.)

**Three event types skip the queued phase:** `user.define_outcome`, `user.custom_tool_result`, and `user.tool_result` are processed on receipt and echoed back with `processed_at` already populated. A pending → acknowledged UI that assumes "first sighting is always `null`" will never clear for these — treat a populated `processed_at` on first sighting as immediately acknowledged.

---

## 3. Interrupt a running session

Send `user.interrupt` as a normal event. The session keeps running until it reaches a safe boundary, then goes idle.

---

## 4. `tool_confirmation` round-trip

When the agent has `permission_policy: { type: 'always_ask' }`, any call to that tool fires an `agent.tool_use` event with `evaluated_permission === 'ask'` and the session goes idle waiting for a decision. Respond with `user.tool_confirmation`.

Key points:
- `tool_use_id` is `event.id` (typically `sevt_...`), **not** a `toolu_...` ID.
- `result` is `'allow' | 'deny'`. Use `deny_message` to tell the model *why* you denied — it gets surfaced back to the agent.
- Multiple pending tools: respond once per `agent.tool_use` event with `evaluated_permission === 'ask'`.

---

## 5. Correct idle-break gate

Do not break on `session.status_idle` alone. The session goes idle transiently — e.g. between parallel tool executions, while waiting for a `user.tool_confirmation`, or while awaiting a `user.custom_tool_result`. Break when idle with a non-`requires_action` `stop_reason` (terminal, or `budget_reached` — resumable only by a budget update, so break unless you intend to change or remove the budget), or on `session.status_terminated`.

`stop_reason.type` values on `session.status_idle`:
- `requires_action` — agent is waiting on a client-side event (tool confirmation, custom tool result). Handle it, don't break.
- `retries_exhausted` — terminal failure. Break, then check `sessions.retrieve()` for the error state.
- `end_turn` — normal completion.
- `budget_reached` — the session hit its spend cap and paused. Not terminal and not resumable by any event: change (typically raise) or remove the session's `budget` to resume, or treat it as done. A `session.usage` event with the final cost immediately precedes this idle. See `shared/managed-agents-core.md` § Session budgets.

---

## 6. Post-idle status-write race

The SSE stream emits `session.status_idle` slightly before the session's queryable status reflects it. Clients that break on idle and immediately call `sessions.delete()` or `sessions.archive()` will intermittently 400 with "cannot delete/archive while running."

Poll before cleanup:

```ts
let s
for (let i = 0; i < 10; i++) {
  s = await client.beta.sessions.retrieve(session.id)
  if (s.status !== 'running') break
  await new Promise(r => setTimeout(r, 200))
}
if (s?.status !== 'running') {
  await client.beta.sessions.archive(session.id)
} // else: still running after 2s — don't archive, let it settle or escalate
```

---

## 8. File-mount gotchas

**The mounted resource has a different `file_id` than the file you uploaded.** Session creation makes a session-scoped copy.

Delete the original via `files.delete(uploaded.id)`; the session-scoped copy is garbage-collected with the session.

---

## 9. Secrets for non-MCP APIs and CLIs — keep them host-side via custom tools

**Do not embed API keys in the system prompt or user messages as a workaround.** Prompts and messages are stored in the session's event history, returned by `events.list()`, and included in compaction summaries — a secret placed there is durably persisted and readable via the API for the life of the session.
