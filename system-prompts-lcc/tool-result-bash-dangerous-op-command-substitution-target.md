<!--
name: 'Tool Result: Bash dangerous operation — command substitution target'
description: >-
  Dangerous rm ask message for a removal target that is the output of a command
  substitution and cannot be checked beforehand. It tells the model to run the
  substitution first and then remove the literal paths it prints.
ccVersion: 2.1.281
-->
Dangerous rm operation detected: the target is the output of a command substitution (`$(...)` or backticks) and cannot be checked before the command runs. This requires explicit approval and cannot be auto-allowed by permission rules.

Run the substitution on its own first, then remove the literal paths it prints.
