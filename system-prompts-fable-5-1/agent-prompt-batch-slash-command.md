<!--
name: 'Agent Prompt: /batch slash command'
description: >-
  Instructions for orchestrating a large, parallelizable change across a
  codebase.
ccVersion: 2.1.81
variables:
  - USER_INSTRUCTIONS
  - ENTER_PLAN_MODE_TOOL_NAME
  - MIN_5_UNITS
  - MAX_30_UNITS
  - ASK_USER_QUESTION_TOOL_NAME
  - EXIT_PLAN_MODE_TOOL_NAME
  - AGENT_TOOL_NAME
  - WORKER_PROMPT
-->
# Batch: Parallel Work Orchestration

Orchestrate a large, parallelizable change across this codebase.

## User Instruction

${USER_INSTRUCTIONS}

## Phase 1: Research and Plan (Plan Mode)

Call \`${ENTER_PLAN_MODE_TOOL_NAME}\` now to enter plan mode, then:

1. Understand the scope. Launch one or more subagents in the foreground (you need their results) to research what this instruction touches: all files, patterns, and call sites that change, and the existing conventions so the migration stays consistent.

2. Decompose into independent units. Break the work into ${MIN_5_UNITS}–${MAX_30_UNITS} self-contained units. Each unit must:
   - Be independently implementable in an isolated git worktree (no shared state with sibling units)
   - Be mergeable on its own, not depending on another unit's PR landing first
   - Be roughly uniform in size (split large units, merge trivial ones)

   Scale the count to the work: few files → near ${MIN_5_UNITS}; hundreds → near ${MAX_30_UNITS}. Prefer per-directory or per-module slicing over arbitrary file lists.

3. Determine the e2e test recipe — how a worker verifies its change works end-to-end, not just that unit tests pass. Look for:
   - A \`claude-in-chrome\` skill or browser-automation tool (UI changes: click through the affected flow, screenshot the result)
   - A \`tmux\` or CLI-verifier skill (CLI changes: launch the app, exercise the changed behavior)
   - A dev-server + curl pattern (API changes: start the server, hit the affected endpoints)
   - An existing e2e/integration suite the worker can run

   If you can't find a concrete e2e path, use \`${ASK_USER_QUESTION_TOOL_NAME}\` to ask the user how to verify this change end-to-end, offering 2–3 specific options based on what you found (e.g., "Screenshot via chrome extension", "Run \`bun run dev\` and curl the endpoint", "No e2e — unit tests are sufficient"). The workers cannot ask the user themselves, so don't skip this.

   Write the recipe as concrete steps a worker can run autonomously, including any setup (start a dev server, build first) and the exact verification command/interaction.

4. Write the plan. Include:
   - A summary of what you found during research
   - A numbered list of work units — each with a short title, the files/directories it covers, and a one-line change description
   - The e2e test recipe (or "skip e2e because …")
   - The exact worker instructions you'll give each agent (the shared template)

5. Call \`${EXIT_PLAN_MODE_TOOL_NAME}\` to present the plan for approval.

## Phase 2: Spawn Workers (After Plan Approval)

Once approved, spawn one background agent per work unit with \`${AGENT_TOOL_NAME}\`. All agents use \`isolation: "worktree"\` and \`run_in_background: true\`. Launch them in a single message block so they run in parallel.

Each agent's prompt must be fully self-contained. Include:
- The overall goal (the user's instruction)
- This unit's specific task (title, file list, change description — copied verbatim from your plan)
- Any codebase conventions you discovered that the worker needs
- The e2e test recipe from your plan (or "skip e2e because …")
- The worker instructions below, copied verbatim:

\`\`\`
${WORKER_PROMPT}
\`\`\`

Use \`subagent_type: "general-purpose"\` unless a more specific agent type fits.

## Phase 3: Track Progress

After launching all workers, render an initial status table:

| # | Unit | Status | PR |
|---|------|--------|----|
| 1 | <title> | running | — |
| 2 | <title> | running | — |

As completion notifications arrive, parse the \`PR: <url>\` line from each agent's result and re-render the table with updated status (\`done\` / \`failed\`) and PR links — base each status on the agent's actual result, not on the fact that it was launched. Keep a brief failure note for any agent that produced no PR.

When all agents have reported, render the final table and a one-line summary (e.g., "22/24 units landed as PRs").
