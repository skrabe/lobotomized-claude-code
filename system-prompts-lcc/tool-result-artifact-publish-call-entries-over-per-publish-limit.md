<!--
name: 'Tool Result: Artifact publish call lists too many entries for one publish'
description: >-
  Error saying file_path and files list more entries than one publish may send,
  nothing was published, and to send at most the limit now and add the rest with
  another publish to the same url
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_2
  - TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_3
  - TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_4
-->
${TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_0?"`file_path` and `files` list":"`files` lists"} ${TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_1} entries (${TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_2>0?"copies and ":""}removals included), over the limit of ${TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_3} one publish may send. Nothing was published: send at most ${TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_3} now and add the rest with another publish to the same url — files left out of a later publish are kept, and a version holds up to ${TOOL_RESULT_ARTIFACT_PUBLISH_CALL_ENTRIES_OVER_PER_PUBLISH_LIMIT_VAR_4} in all.
