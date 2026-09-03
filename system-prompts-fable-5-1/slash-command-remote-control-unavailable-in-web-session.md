<!--
name: 'Slash Command: Remote Control Unavailable In Web Session'
description: >-
  Reply emitted as local-command-stdout when /remote-control is invoked from a
  session already running in Claude Code on the web.
ccVersion: 2.1.224
variables:
  - SLASH_COMMAND_REMOTE_CONTROL_UNAVAILABLE_IN_WEB_SESSION_VAR_0
  - SLASH_COMMAND_REMOTE_CONTROL_UNAVAILABLE_IN_WEB_SESSION_VAR_1
-->
Remote Control connects a terminal session to claude.ai, and this session is already running in Claude Code on the web: ${SLASH_COMMAND_REMOTE_CONTROL_UNAVAILABLE_IN_WEB_SESSION_VAR_0(SLASH_COMMAND_REMOTE_CONTROL_UNAVAILABLE_IN_WEB_SESSION_VAR_1)}.
