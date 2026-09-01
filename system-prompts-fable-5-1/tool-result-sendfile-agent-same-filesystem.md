<!--
name: 'Tool result: SendFile target is a same-session agent'
description: >-
  SendFile refused-result telling the model that a same-session agent already
  shares the filesystem and to use the message tool with @path instead.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_SENDFILE_AGENT_SAME_FILESYSTEM_VAR_0
  - TOOL_RESULT_SENDFILE_AGENT_SAME_FILESYSTEM_VAR_1
  - TOOL_RESULT_SENDFILE_AGENT_SAME_FILESYSTEM_VAR_2
-->
'${TOOL_RESULT_SENDFILE_AGENT_SAME_FILESYSTEM_VAR_0}' is an agent in this session — it already shares your filesystem, so there is nothing to transfer. Use ${TOOL_RESULT_SENDFILE_AGENT_SAME_FILESYSTEM_VAR_1} and reference the file as @<path> instead. ${TOOL_RESULT_SENDFILE_AGENT_SAME_FILESYSTEM_VAR_2} is for OTHER Claude Code sessions (a peer session on this machine, or a Remote Control / cloud session).
