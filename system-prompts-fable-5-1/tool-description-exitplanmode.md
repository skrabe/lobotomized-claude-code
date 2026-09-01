<!--
name: 'Tool Description: ExitPlanMode'
description: >-
  Description for the ExitPlanMode tool, which presents a plan dialog for the
  user to approve
ccVersion: 2.1.205
variables:
  - ASK_USER_QUESTION_TOOL_NAME
-->

Use when you're in plan mode, have finished writing your plan to the plan file (named in the plan-mode system message), and are ready for user approval. It reads the plan from that file — it does not take plan content as a parameter — and signals you're done planning so the user can review and approve.

ExitPlanMode also provides a cancellation outcome that exits plan mode without submitting a plan or requesting implementation approval.

Use only when planning the implementation steps of a task that requires writing code. For research tasks (gathering information, searching/reading files, understanding the codebase), don't use this tool.

Don't use AskUserQuestion to ask "Is this plan okay?" or "Should I proceed?" — ExitPlanMode is what requests approval. (Use AskUserQuestion earlier to resolve open requirements before finalizing the plan.)
