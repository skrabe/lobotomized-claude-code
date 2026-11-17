<!--
name: PowerShell alias-shadows-function deny
description: >-
  PowerShell deny message when a defined function's name is shadowed by a
  built-in alias.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_POWERSHELL_ALIAS_SHADOWS_FUNCTION_REFUSED_VAR_0
-->
The command was not run. ${TOOL_RESULT_POWERSHELL_ALIAS_SHADOWS_FUNCTION_REFUSED_VAR_0}. PowerShell runs an alias before a function, so a call by such a name runs what the alias names, not the function defined here. Rename the function, for example with a Verb-Noun name, and change every call to the new name. Keeping the name is not safe: after Set-Alias, with an [Alias()] attribute, in a script file or after removing the alias, the built-in can still run. Any command that defines this name is refused.
