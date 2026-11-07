<!--
name: 'Tool Result: ProposeSkills edit not found, read file'
description: >-
  Validation problem when an edit's text is absent from the skill's SKILL.md and
  the file path is known: read the file and resend matching edits or the full
  skillMd.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_PROPOSESKILLS_EDIT_NOT_FOUND_READ_FILE_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_EDIT_NOT_FOUND_READ_FILE_VAR_1
-->
${TOOL_RESULT_PROPOSESKILLS_EDIT_NOT_FOUND_READ_FILE_VAR_0} (${TOOL_RESULT_PROPOSESKILLS_EDIT_NOT_FOUND_READ_FILE_VAR_1}). Read that file, then call again with edits that match it, or with the complete skillMd.
