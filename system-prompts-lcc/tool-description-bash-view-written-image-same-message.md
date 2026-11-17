<!--
name: 'Tool Description: Bash view written image in same message'
description: >-
  Bash prompt bullet: to see an image a command will write, call the read tool
  on its path right after the Bash call in the same message, not for commands
  that may outlast the timeout.
ccVersion: 2.1.326
variables:
  - TOOL_DESCRIPTION_BASH_VIEW_WRITTEN_IMAGE_SAME_MESSAGE_VAR_0
  - TOOL_DESCRIPTION_BASH_VIEW_WRITTEN_IMAGE_SAME_MESSAGE_VAR_1
  - TOOL_DESCRIPTION_BASH_VIEW_WRITTEN_IMAGE_SAME_MESSAGE_VAR_2
-->
- If you need to see a picture that a command will write and you know its path, call ${TOOL_DESCRIPTION_BASH_VIEW_WRITTEN_IMAGE_SAME_MESSAGE_VAR_0} on that path in the same message, right after the ${TOOL_DESCRIPTION_BASH_VIEW_WRITTEN_IMAGE_SAME_MESSAGE_VAR_1} call. The calls run in order, so a command that finishes in the foreground will have written the file. Don't do this with ${TOOL_DESCRIPTION_BASH_VIEW_WRITTEN_IMAGE_SAME_MESSAGE_VAR_2?"`run_in_background` or a command":"a command"} that may outlast its \`timeout\`.
