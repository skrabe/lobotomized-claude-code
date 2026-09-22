<!--
name: Multiple matches but replace_all false
description: >-
  Edit tool error returned to the model when old_string matches multiple times
  without replace_all.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_EDIT_MULTIPLE_MATCHES_VAR_0
  - TOOL_RESULT_EDIT_MULTIPLE_MATCHES_VAR_1
-->
Found ${TOOL_RESULT_EDIT_MULTIPLE_MATCHES_VAR_0} matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String: ${TOOL_RESULT_EDIT_MULTIPLE_MATCHES_VAR_1}
