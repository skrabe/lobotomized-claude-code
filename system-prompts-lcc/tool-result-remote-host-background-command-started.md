<!--
name: 'Remote Host: Background Command Started'
description: >-
  Tool result a serving computer returns to a cloud session for a shell command
  started in the background: its ID and output file, that the session is not
  notified on completion, how to tell it ended, and its time limit.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_1
  - TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_2
  - TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_3
-->
Command running in the background on ${TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_0} with ID: ${TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_1}. Output is being written there to: ${TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_2}. This session is not notified when it finishes. Whether it is still running is told by ${TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_0} itself: not by that file, which holds only what the command has printed (a program that buffers its output shows it there only when it flushes), and never by pgrep, ps, pkill or a network request from a later command, because where ${TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_0} sandboxes commands each command sees only its own processes and its own network, so a command that is running looks absent from there. It is stopped after ${TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_3} in the background, or earlier if ${TOOL_RESULT_REMOTE_HOST_BACKGROUND_COMMAND_STARTED_VAR_0} stops serving this session.
