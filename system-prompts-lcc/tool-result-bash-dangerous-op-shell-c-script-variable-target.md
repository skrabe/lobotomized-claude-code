<!--
name: 'Tool Result: Bash dangerous operation shell -c variable target'
description: >-
  Ask message for an rm inside a shell -c script whose target is built from a
  variable or command output known only at run time, requiring explicit approval
  and suggesting a literal path or a ${NAME:?} guard.
ccVersion: 2.1.288
-->
Dangerous rm operation in a shell -c script: its target is built from a variable or command output known only when it runs, and if that is empty the rm can reach a directory like / or your home directory. This requires explicit approval and cannot be auto-allowed by permission rules. Pass a literal path, or guard the value with ${NAME:?}.
