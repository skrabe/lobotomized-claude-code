<!--
name: 'Tool result: remote host sandbox confines files and network'
description: >-
  First-time note on a remote-host command result that the host's sandbox hides
  denied paths, blocks writes outside the working folders and limits network
  hosts, so missing things may be the sandbox.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_REMOTE_HOST_SANDBOX_FILES_AND_NETWORK_CONFINED_VAR_0
-->
Commands this session runs on ${TOOL_RESULT_REMOTE_HOST_SANDBOX_FILES_AND_NETWORK_CONFINED_VAR_0} run inside Claude Code's sandbox there. A path its settings deny looks missing or empty to them, writes outside the working folders fail, and only allowed network hosts are reachable. If something you expect is absent, say it may be the sandbox rather than working around it.
