<!--
name: Local Command Stdout Framing Tag
description: >-
  Model-facing framing tag wrapping a forked/local slash-command's stdout into a
  user-role message sent to the model
  ("<local-command-stdout>\n${out}\n</local-command-stdout>"); present whenever
  a local command produces output that is fed back to the model.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_LOCAL_COMMAND_STDOUT_FRAMING_TAG_VAR_0
  - SYSTEM_PROMPT_LOCAL_COMMAND_STDOUT_FRAMING_TAG_VAR_1
  - SYSTEM_PROMPT_LOCAL_COMMAND_STDOUT_FRAMING_TAG_VAR_2
-->
<local-command-stdout>${SYSTEM_PROMPT_LOCAL_COMMAND_STDOUT_FRAMING_TAG_VAR_0(SYSTEM_PROMPT_LOCAL_COMMAND_STDOUT_FRAMING_TAG_VAR_1(SYSTEM_PROMPT_LOCAL_COMMAND_STDOUT_FRAMING_TAG_VAR_2.displayText))}</local-command-stdout>
