<!--
name: 'Statusline setup: Windows path note'
description: >-
  Windows-specific instruction injected into the statusline-setup system prompt
  telling the model to use forward slashes in command file paths.
ccVersion: 2.1.206
-->

   On Windows, write any file path inside the "command" string with forward slashes
   (for example C:/Users/me/.claude/statusline.ps1) or the ~ shorthand. Do not use
   backslashes: the command is executed through Git Bash, which consumes unquoted
   backslashes as escape characters and the path will not resolve.
