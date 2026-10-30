<!--
name: 'Tool result: remote host sandbox denied paths clause'
description: >-
  Clause naming the paths the remote host's sandbox settings deny, saying they
  look missing or empty and telling the model not to substitute another file but
  to tell the user they are blocked.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_1
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_2
-->
${TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_0} (its settings deny ${TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_1?"that path":"those paths"}). In this command ${TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_1?"that path looks":"those paths look"} missing or empty even if ${TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_1?"it exists":"they exist"} on ${TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_2}. Do not substitute another file for ${TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_1?"it":"them"}: tell the user ${TOOL_RESULT_REMOTE_HOST_SANDBOX_DENIED_PATHS_CLAUSE_VAR_1?"it is":"they are"} blocked.
