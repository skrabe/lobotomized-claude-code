<!--
name: 'Tool result: remote host sandbox may not be starting'
description: >-
  Clause appended to a remote-host command result when its output is only a
  bwrap/sandbox-exec error, telling the model a rerun will not help and to tell
  the user the sandbox may not be starting.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_UNAVAILABLE_CLAUSE_VAR_0
-->
 Its output is only a bwrap or sandbox-exec error, which usually means the sandbox could not start and the command never ran. If so, running it again will not help: tell the user the sandbox on ${TOOL_RESULT_REMOTE_HOST_SANDBOX_UNAVAILABLE_CLAUSE_VAR_0} may not be starting.
