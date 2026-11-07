<!--
name: 'System Reminder: Approved Claude Doc plan readback'
description: >-
  Requires reading every body of the approved Claude Doc before implementation,
  treating user edits as the plan and asking permission before falling back to
  memory after two failed reads
ccVersion: 2.1.319
variables:
  - FORMAT_PLAN_DOC_LABEL_FN
  - APPROVED_PLAN_DOC
-->
The approved plan is ${FORMAT_PLAN_DOC_LABEL_FN(APPROVED_PLAN_DOC)}, as the user left it when they approved. They may have changed it after you last wrote it, up to that moment, so what you remember writing may not be what they approved.
