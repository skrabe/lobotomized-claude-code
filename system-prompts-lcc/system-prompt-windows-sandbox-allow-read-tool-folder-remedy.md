<!--
name: 'System Prompt: Windows sandbox allowRead tool folder remedy'
description: >-
  Remedy clause telling the user how to make tool directories readable or add a
  tool folder to sandbox.filesystem.allowRead and restart
ccVersion: 2.1.325
variables:
  - SYSTEM_PROMPT_WINDOWS_SANDBOX_ALLOW_READ_TOOL_FOLDER_REMEDY_VAR_0
  - SYSTEM_PROMPT_WINDOWS_SANDBOX_ALLOW_READ_TOOL_FOLDER_REMEDY_VAR_1
-->
${SYSTEM_PROMPT_WINDOWS_SANDBOX_ALLOW_READ_TOOL_FOLDER_REMEDY_VAR_0}, which makes the tool directories named above readable where set-up has not done that yet, or they can add that tool's own folder to \`sandbox.filesystem.allowRead\` in ${SYSTEM_PROMPT_WINDOWS_SANDBOX_ALLOW_READ_TOOL_FOLDER_REMEDY_VAR_1} (as \`~/...\`, which in a settings file is the user's home, or a full path with backslashes doubled) and restart Claude Code (an administrator's policy can overrule the entry); sandboxed commands can then read and run everything in it
