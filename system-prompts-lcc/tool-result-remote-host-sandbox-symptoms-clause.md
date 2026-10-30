<!--
name: 'Tool result: remote host sandbox refusal symptoms clause'
description: >-
  Clause listing what a remote-host command's output says (sandbox refusal
  symptoms) and that rerunning unchanged will fail the same way.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_1
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_2
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_3
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_4
-->
 Its output says ${TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_0.map((TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_1)=>TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_2[TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_1]).join(" and ")}, which there usually means the sandbox refused it${TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_3}, and if so running it again unchanged will fail the same way.${TOOL_RESULT_REMOTE_HOST_SANDBOX_SYMPTOMS_CLAUSE_VAR_4}
