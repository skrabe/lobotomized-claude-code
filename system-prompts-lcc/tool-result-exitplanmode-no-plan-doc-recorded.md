<!--
name: 'Tool Result: ExitPlanMode no plan Doc recorded'
description: >-
  Validation error when no Claude Doc is recorded for the plan: create the Doc
  with the reminder's exact call then call with no argument, or pass the whole
  plan as the only argument
ccVersion: 2.1.317
-->
No plan Doc is recorded for this session: none was created, or it was created with arguments other than the ones that plan mode's reminder shows. If you created none, create it with exactly that call and then call this tool with no argument. If you already created one, pass the whole plan as non-empty text in `plan` as the only argument, so that the user is not left with two Docs.
