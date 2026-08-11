<!--
name: 'Tool Parameter: ProposeGoal Condition'
description: >-
  Describes the verifiable completion-condition parameter in the ProposeGoal
  tool schema sent to the model.
ccVersion: 2.1.227
variables:
  - TOOL_PARAMETER_PROPOSEGOAL_CONDITION_VAR_0
-->
The completion condition to propose, written so a separate evaluator can verify it from the conversation (e.g. "all tests in test/auth pass (bun test exits 0)"). At most ${TOOL_PARAMETER_PROPOSEGOAL_CONDITION_VAR_0} characters — the user must be able to read the whole condition in the approval dialog.
