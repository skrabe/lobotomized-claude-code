<!--
name: 'Tool Result: ProposeSkills edits on old copy'
description: >-
  Validation problem when edits target a SKILL.md that differs from Claude's
  last proposal (unsaved/stale), asking to read the file and resend edits
  including unsaved changes.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_1
  - TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_2
  - TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_3
  - TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_4
-->
${TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_0(TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_1)}: the user did not save it, the save is not here yet, or the skill changed after it. Edits apply to that file alone. ${TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_2!==void 0?"Read it, then call":TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_3===void 0?"Call":`${TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_3}.${TOOL_RESULT_PROPOSESKILLS_EDITS_ON_OLD_COPY_VAR_4}Call`} again with edits. Include the changes of your last proposal that the file lacks, unless the user turned them down.
