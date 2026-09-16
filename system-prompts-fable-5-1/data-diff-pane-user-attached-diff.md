<!--
name: Diff Pane User Attached Diff
description: >-
  Prompt context injected on prompt.submit when the user arms a file diff from
  the /diff pane.
ccVersion: 2.1.273
variables:
  - DATA_DIFF_PANE_USER_ATTACHED_DIFF_VAR_0
  - DATA_DIFF_PANE_USER_ATTACHED_DIFF_VAR_1
-->
The user attached the diff of ${DATA_DIFF_PANE_USER_ATTACHED_DIFF_VAR_0} from the diff pane to this prompt:
${DATA_DIFF_PANE_USER_ATTACHED_DIFF_VAR_1.join(`
`)}
