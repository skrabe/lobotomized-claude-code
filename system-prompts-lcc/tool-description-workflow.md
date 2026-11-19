<!--
name: 'Tool Description: Workflow'
description: >-
  Trimmed 2026-09-02: the meta/script-API paragraph and the example script are
  carried by the workflow-authoring skill, which the description tells the model
  to load before writing a script. The opt-in gate is kept via the
  WORKFLOW_OPT_IN_GUIDANCE_FN slot (its text is
  tool-description-workflow-lean-rewrite).
ccVersion: 2.1.328
variables:
  - WORKFLOW_OPT_IN_GUIDANCE_FN
  - SYSTEM_MESSAGE_PHRASE
-->
Execute a workflow script that orchestrates multiple subagents deterministically. Workflows run in the background — this tool returns immediately with a task ID, and a <task-notification> arrives when the workflow completes. Use /workflows to watch live progress.

${WORKFLOW_OPT_IN_GUIDANCE_FN(SYSTEM_MESSAGE_PHRASE)}

Pass the script inline via \`script\` (plain JavaScript, starting with a pure-literal \`export const meta = {...}\`); do not also set the tool's \`name\` input, which selects a saved workflow.
