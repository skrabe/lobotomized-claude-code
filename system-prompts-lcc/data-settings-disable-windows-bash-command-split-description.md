<!--
name: 'Data: disableWindowsBashCommandSplit setting description'
description: >-
  Description of the `disableWindowsBashCommandSplit` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.319
-->
Windows only. Set to true to keep every Bash command in a single argument to bash, so that endpoint security tools that match text in process command lines see it whole. Otherwise Claude Code may split a long command over several arguments. With true, a command of about 7,000 characters or more, or fewer if it is full of quotes, may reach bash cut short, and then usually fails with a syntax error. Only honored from managed settings; ignored in user, project, local and --settings sources.
