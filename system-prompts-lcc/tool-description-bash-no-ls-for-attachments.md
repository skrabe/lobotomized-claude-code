<!--
name: 'Bash tool: don''t ls/find for attached files'
description: >-
  Gated Bash tool description bullet telling the model not to run ls/find to
  check for attachments; attached files are named in their message.
ccVersion: 2.1.318
-->
- Don't run `ls` or `find` to see whether the person attached a file. Each attached file is named in the message that it came with; if no message names one, none came.
