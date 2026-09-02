<!--
name: 'Tool Description: Workflow'
description: >-
  Trimmed 2026-09-02: the meta/script-API paragraph and the example script are carried by the workflow-authoring skill, which the description tells the model to load before writing a script. The opt-in gate is kept verbatim.
ccVersion: 2.1.251
variables:
  - AGENT_TOOL_NAME
-->
Execute a workflow script that orchestrates multiple subagents deterministically. Workflows run in the background — this tool returns immediately with a task ID, and a <task-notification> arrives when the workflow completes. Use /workflows to watch live progress.

ONLY call this tool when the user has explicitly opted into multi-agent orchestration. Workflows can spawn dozens of agents and consume a large amount of tokens; the user must request that scale, not have it inferred. Explicit opt-in means one of:
- The user included the keyword "ultracode" in their prompt (you'll see a system-reminder confirming it).
- Ultracode is on for the session (a system-reminder confirms it) — see **Ultracode** in the workflow authoring reference.
- The user directly asked you to run a workflow or use multi-agent orchestration in their own words ("use a workflow", "run a workflow", "fan out agents", "orchestrate this with subagents"). The ask must be in the user's words — a task that would merely benefit from a workflow does not count.
- The user invoked a skill or slash command whose instructions tell you to call Workflow.
- The user asked you to run a specific named or saved workflow.

For any other task — even one that would clearly benefit from parallelism — do NOT call this tool. Use the ${AGENT_TOOL_NAME} tool (if available) for individual subagents, or briefly describe what a multi-agent workflow could do and how much it would roughly cost, and ask the user whether to run it. Mention they can ask for one with "use a workflow" in a future message to skip the ask.

Pass the script inline via \`script\` (plain JavaScript, starting with a pure-literal \`export const meta = {...}\`); do not also set the tool's \`name\` input, which selects a saved workflow.
