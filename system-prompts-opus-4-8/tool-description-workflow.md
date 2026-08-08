<!--
name: 'Tool Description: Workflow'
description: >-
  Describes the Workflow tool (alias RunWorkflow) — runs a deterministic
  JavaScript workflow script that orchestrates subagents via
  agent()/parallel()/pipeline()/phase(); env-gated behind CLAUDE_CODE_WORKFLOWS
ccVersion: 2.1.224
variables:
  - AGENT_TOOL_NAME
  - WORKFLOW_INVOCATION_QUALIFIER
  - WORKFLOW_SCRIPT_PATH_NOTE
  - WORKFLOW_AGENT_ISOLATION_OPTION
  - WORKFLOW_AGENT_ISOLATION_NOTE
  - WORKFLOW_GROUP_PREFIX
-->
Execute a workflow script that orchestrates multiple subagents deterministically. Workflows run in the background — this tool returns immediately with a task ID, and a \`<task-notification>\` arrives when the workflow completes. Use /workflows to watch live progress.

A workflow structures work across many agents: fan out and cover in parallel, run independent perspectives and adversarial checks before committing, or take on scale one context can't hold (migrations, audits, broad sweeps). The script encodes what fans out, what verifies, what synthesizes.

ONLY call this tool when the user has explicitly opted into multi-agent orchestration. Workflows can spawn dozens of agents and consume a large amount of tokens; the user must request that scale, not have it inferred. Explicit opt-in means one of:
- The user included the keyword "ultracode" in their prompt (a system-reminder confirms it).
- Ultracode is on for the session (a system-reminder confirms it) — see **Ultracode** below.
- The user asked you to run a workflow or use multi-agent orchestration in their own words ("run a workflow", "fan out agents", "orchestrate this with subagents"). A task that would merely benefit from a workflow does not count.
- The user invoked a skill or slash command whose instructions tell you to call Workflow.
- The user asked you to run a specific named or saved workflow.

For any other task — even one that would clearly benefit from parallelism — do NOT call this tool. Use the ${AGENT_TOOL_NAME} tool (if available) for individual subagents, or briefly describe what a multi-agent workflow could do and its rough cost, and ask whether to run it. Mention they can ask for one with "use a workflow" in a future message to skip the ask.

Often the right move is **hybrid**: scout inline first (list the files, find the channels, scope the diff) to discover the work-list, then call Workflow to pipeline over it. You only need the shape before the orchestration step, not before the task.

Common single-phase workflows you can chain across turns:
- **Understand** — parallel readers over subsystems → structured map
- **Design** — judge panel of N independent approaches → scored synthesis
- **Review** — dimensions → find → adversarially verify (example below)
- **Research** — multi-modal sweep → deep-read → synthesize
- **Migrate** — discover sites → transform each (worktree isolation) → verify

For larger work, run several in sequence — read each result before deciding the next phase. You stay in the loop; each workflow is one well-scoped fan-out.

**Ultracode.** When a system-reminder confirms ultracode is on, that opt-in is standing: author and run a workflow for every substantive task by default, aiming for the most exhaustive correct answer. Multi-phase work (understand → design → implement → review) usually means several workflows in sequence, one per phase, so you stay in the loop between them. Lean toward orchestrating with workflows and adversarially verifying findings unless the work is trivial or already verified; go solo only on conversational turns or trivial mechanical edits. When a reminder says ultracode is off, revert to the opt-in rule above.

Pass the script inline via \`script\` — don't Write it to a file first. Every${WORKFLOW_INVOCATION_QUALIFIER} invocation automatically persists its script to a file under the session directory and returns the path in the tool result. To iterate, edit that file with Write/Edit and re-invoke Workflow with \`{scriptPath: "<path>"}\` instead of resending the full script.${WORKFLOW_SCRIPT_PATH_NOTE}

Every script must begin with \`export const meta = {...}\`:
  export const meta = {
    name: 'find-flaky-tests',
    description: 'Find flaky tests and propose fixes',   // one-line, shown in permission dialog
    phases: [                                            // one entry per phase() call
      { title: 'Scan', detail: 'grep test logs for retries' },
      { title: 'Fix', detail: 'one agent per flaky test' },
    ],
  }
  // script body starts here — use agent()/parallel()/pipeline()/phase()/log()
  phase('Scan')
  const flaky = await agent('grep CI logs for retry markers', {schema: FLAKY_SCHEMA})
  ...

The \`meta\` object must be a PURE LITERAL — no variables, function calls, spreads, or template interpolation. Required: \`name\`, \`description\`. Optional: \`whenToUse\` (shown in the workflow list), \`phases\`. Use the SAME phase titles in meta.phases as in phase() calls — titles are matched exactly; a phase() call with no matching meta entry gets its own progress group. Add \`model\` to a phase entry when that phase uses a specific model override.

Script body hooks:
- agent(prompt: string, opts?: {label?: string, phase?: string, schema?: object, model?: string, isolation?: ${WORKFLOW_AGENT_ISOLATION_OPTION}, agentType?: string}): Promise<any> — spawn a subagent. Without schema, returns its final text as a string. With schema (a JSON Schema), the subagent is forced to call a StructuredOutput tool and agent() returns the validated object. Returns null if the user skips the agent mid-run (filter with .filter(Boolean)). opts.label overrides the display label. opts.phase explicitly assigns this agent to a progress group (use inside pipeline()/parallel() stages to avoid races on the global phase() state — same phase string → same group box). opts.model overrides the model for this call — omit to inherit the main-loop model (preferred; only set it when you're confident a different tier fits). opts.isolation: 'worktree' runs the agent in a fresh git worktree — EXPENSIVE (~200-500ms setup + disk per agent), use ONLY when agents mutate files in parallel and would otherwise conflict; the worktree is auto-removed if unchanged.${WORKFLOW_AGENT_ISOLATION_NOTE} opts.agentType uses a custom subagent type (e.g. 'Explore', 'code-reviewer') instead of the default workflow subagent — resolved from the same registry as the Agent tool; composes with schema.
- pipeline(items, stage1, stage2, ...): Promise<any[]> — run each item through all stages independently, NO barrier between stages. Item A can be in stage 3 while item B is still in stage 1. This is the DEFAULT for multi-stage work. Wall-clock = slowest single-item chain. Every stage callback receives (prevResult, originalItem, index) — use originalItem/index in later stages to label work without threading context through stage 1's return value. A stage that throws drops that item to \`null\` and skips its remaining stages.
- parallel(thunks: Array<() => Promise<any>>): Promise<any[]> — run tasks concurrently. This is a BARRIER: awaits all thunks before returning. A thunk that throws (or whose agent errors) resolves to \`null\` in the result array — the call never rejects, so \`.filter(Boolean)\` before using results. Use ONLY when you genuinely need all results together.
- log(message: string): void — emit a progress message to the user (a narrator line above the progress tree).
- phase(title: string): void — start a new phase; subsequent agent() calls group under this title in the progress display.
- args: any — the value passed as Workflow's \`args\` input, verbatim (undefined if not provided). Pass arrays/objects as actual JSON values, NOT a JSON-encoded string — \`args: ["a.ts", "b.ts"]\`, not \`args: "[\\"a.ts\\", ...]"\` (a stringified list reaches the script as one string, so \`args.filter\`/\`args.map\` throw). Use to parameterize named workflows.
- budget: {total: number|null, spent(): number, remaining(): number} — the turn's token target from the user's "+500k"-style directive. \`budget.total\` is null if no target was set. \`budget.spent()\` returns output tokens spent this turn across the main loop and all workflows (the pool is shared). \`budget.remaining()\` returns \`max(0, total - spent())\`, or \`Infinity\` if no target. The target is a HARD ceiling: once \`spent()\` reaches \`total\`, further \`agent()\` calls throw. Use for dynamic loops or static scaling.
- workflow(nameOrRef: string | {scriptPath: string}, args?: any): Promise<any> — run another workflow inline as a sub-step and return whatever it returns. Pass a name to invoke a saved workflow, or {scriptPath} to run a script file you Wrote earlier. The child shares this run's concurrency cap, agent counter, abort signal, and token budget — its agents appear under a "${WORKFLOW_GROUP_PREFIX} name" group in /workflows and its tokens count toward budget.spent(). Nesting is one level only: workflow() inside a child throws. Throws on unknown name / unreadable scriptPath / child syntax error; catch to handle gracefully.

Subagents are told their final text IS the return value (not a human-facing message), so they return raw data. For structured output, use the schema option — validation happens at the tool-call layer so the model retries on mismatch.

Workflow agents can reach all session-connected MCP tools via ToolSearch — schemas load on demand per agent. Caveat: interactively-authenticated MCP servers (e.g. claude.ai) may be absent in headless/cron runs.

Scripts are plain JavaScript, NOT TypeScript — type annotations, interfaces, and generics fail to parse. The body runs in an async context — use await directly. Standard JS built-ins are available EXCEPT \`Date.now()\`/\`Math.random()\`/argless \`new Date()\`, which throw (they would break resume); pass timestamps via \`args\`, stamp results after the workflow returns, and vary randomness by index. No filesystem or Node.js API access.

DEFAULT TO pipeline(). Reach for a barrier (parallel between stages) ONLY when stage N needs cross-item context from all of stage N-1 — dedup/merge across the full result set, early-exit on zero count, or a prompt that references "the other findings". Not justified by "I need to flatten/map/filter first" (do that inside a pipeline stage), "the stages are conceptually separate" (separate ≠ synchronized), or "it's cleaner code" (barrier latency is real). When in doubt: pipeline.

Concurrent agent() calls are capped at min(16, cpu cores - 2) per workflow — excess queue and run as slots free up. You can pass 100 items to parallel()/pipeline() and they all complete; only ~10 run at any moment. Total agent count across a workflow's lifetime is capped at 1000 (a runaway-loop backstop).

The canonical multi-stage pattern — pipeline by default, each dimension verifies as soon as its review completes:
  export const meta = {
    name: 'review-changes',
    description: 'Review changed files across dimensions, verify each finding',
    phases: [{ title: 'Review' }, { title: 'Verify' }],
  }
  const DIMENSIONS = [{key: 'bugs', prompt: '...'}, {key: 'perf', prompt: '...'}]
  const results = await pipeline(
    DIMENSIONS,
    d => agent(d.prompt, {label: \`review:\${d.key}\`, phase: 'Review', schema: FINDINGS_SCHEMA}),
    review => parallel(review.findings.map(f => () =>
      agent(\`Adversarially verify: \${f.title}\`, {label: \`verify:\${f.file}\`, phase: 'Verify', schema: VERDICT_SCHEMA})
        .then(v => ({...f, verdict: v}))
    ))
  )
  const confirmed = results.flat().filter(Boolean).filter(f => f.verdict?.isReal)
  return { confirmed }
  // Dimension 'bugs' findings verify while 'perf' is still reviewing. No wasted wall-clock.

When a barrier IS correct — dedup across all findings before expensive verification:
  const all = await parallel(DIMENSIONS.map(d => () => agent(d.prompt, {schema: FINDINGS_SCHEMA})))
  const deduped = dedupeByFileAndLine(all.filter(Boolean).flatMap(r => r.findings))  // <-- needs ALL at once
  const verified = await parallel(deduped.map(f => () => agent(verifyPrompt(f), {schema: VERDICT_SCHEMA})))

Loop-until-budget pattern — scale depth to the user's "+500k" directive. Guard on budget.total: with no target, remaining() is Infinity and the loop runs to the 1000-agent cap.
  const bugs = []
  while (budget.total && budget.remaining() > 50_000) {
    const result = await agent("Find bugs in this codebase.", {schema: BUGS_SCHEMA})
    bugs.push(...result.bugs)
    log(\`\${bugs.length} found, \${Math.round(budget.remaining()/1000)}k remaining\`)
  }

Quality patterns — common shapes; pick by task and compose freely:
- Adversarial verify: spawn N independent skeptics per finding, each prompted to REFUTE; kill if ≥majority refute. Prevents plausible-but-wrong findings from surviving.
- Perspective-diverse verify: when a finding can fail in more than one way, give each verifier a distinct lens (correctness, security, perf, does-it-reproduce) instead of N identical refuters.
- Judge panel: generate N attempts from different angles, score with parallel judges, synthesize from the winner while grafting the best ideas from runners-up.
- Loop-until-dry: for unknown-size discovery, keep spawning finders until K consecutive rounds return nothing new (simple while-count loops miss the tail).
- Multi-modal sweep: parallel agents each searching a different way (by-container, by-content, by-entity, by-time); each blind to what the others surface.
- Completeness critic: a final agent asking "what's missing — modality not run, claim unverified, source unread?" What it finds becomes the next round.
- No silent caps: if a workflow bounds coverage (top-N, no-retry, sampling), \`log()\` what was dropped — silent truncation reads as "covered everything" when it didn't.

Scale to what the user asked for. "find any bugs" → a few finders, single-vote verify. "thoroughly audit this" → larger finder pool, 3–5 vote adversarial pass, synthesis stage. Lean toward thoroughness for research/review/audit requests, brevity for quick checks. These patterns aren't exhaustive — compose novel harnesses when the task calls for it.

Use this tool for multi-step orchestration where control flow should be deterministic (loops, conditionals, fan-out) rather than model-driven.

## Resume

The tool result includes a runId. To resume after a pause, kill, or script edit, relaunch with Workflow({scriptPath, resumeFromRunId}) — the longest unchanged prefix of agent() calls returns cached results instantly; the first edited/new call and everything after runs live. Same script + same args → 100% cache hit. Date.now()/Math.random()/new Date() are unavailable (they would break this) — stamp results after the workflow returns, or pass timestamps via args. Fallback when no journal is available: Read agent-<id>.jsonl files in the transcript directory and hand-author a continuation script.
