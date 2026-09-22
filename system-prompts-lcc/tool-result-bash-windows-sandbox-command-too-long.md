<!--
name: 'Tool Result: Windows Sandbox Command Too Long'
description: >-
  Message of SandboxCommandTooLongError thrown while wrapping a Bash/PowerShell
  command; propagates uncaught to the tool harness and is returned to the model
  as <tool_use_error>, advising it to write the script to a file or split the
  command.
ccVersion: 2.1.214
-->
Command is too long for the Windows sandbox. The limit covers the sandbox arguments too, so trimming just under it will not help; on PowerShell the script is base64-encoded first (~2.7x), leaving ~10,000 characters. Write the script to a file and run that, or split the command up.
