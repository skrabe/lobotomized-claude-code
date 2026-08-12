<!--
name: PR Walkthrough Artifact Command Prompt
description: >-
  getPromptForCommand {type:'text',text:WOf(e)} body for the
  shareable-PR-walkthrough slash command, instructing the model to produce a
  self-contained HTML PR walkthrough page and publish it via the artifact tool.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_0
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_1
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_2
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_3
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_4
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_5
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_6
  - SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_2_VAR_7
-->

${SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_0===""?SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_1:SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_2(SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_0)}
${SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_3?`
Additional guidance from the user: ${SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_3}
`:""}
## Goal

Produce a **shareable PR walkthrough artifact** — a self-contained HTML page a
reviewer can read before opening the diff to understand what this change does,
why it's being made, and where to focus attention. Pitch the writing at a
reviewer seeing this PR for the first time.

## Structure of the artifact

Write an HTML file and publish it with the ${SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_4} tool. Load
the `${SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_5}` skill first and give the page a
utilitarian treatment.

1. **What and why** — two or three sentences: what this PR changes and the
   reason it's needed. If the PR body already says this well, reuse it.
2. **Before / After** — a short side-by-side showing the user-observable
   change (behavior, API shape, or output). Skip if the change has no
   observable surface.
3. **Tour of the diff** — one `<details>` block per logical piece of the
   change. Inside each: the relevant code snippet (trimmed), a plain-language
   explanation of what it does, and anything a reviewer should look closely
   at.
4. **What's not obvious from the diff** — context a reviewer needs that the
   diff alone doesn't show (why this approach over an alternative, what was
   tried and rejected, follow-ups intentionally left out).

End the page body with this line verbatim:

> ${SYSTEM_PROMPT_PR_WALKTHROUGH_ARTIFACT_COMMAND_VAR_6}

## Keep it honest

Describe what the diff *actually does* — trace it, don't infer from names. If
something in the PR is unclear to you, say so in section 4 rather than
guessing.
