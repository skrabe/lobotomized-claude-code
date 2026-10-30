<!--
name: 'Tool result: remote host sandbox violations clause'
description: >-
  Clause on a remote-host command result saying the sandbox_violations lines
  name what was blocked and that rerunning unchanged will fail the same way.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_VIOLATIONS_CLAUSE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_VIOLATIONS_CLAUSE_VAR_1
-->
 The sandbox_violations lines in its output name what it blocked${TOOL_RESULT_REMOTE_HOST_SANDBOX_VIOLATIONS_CLAUSE_VAR_0?", and if that is what failed it, running it again unchanged will fail the same way":", and that stays blocked on a rerun"}.${TOOL_RESULT_REMOTE_HOST_SANDBOX_VIOLATIONS_CLAUSE_VAR_1}
