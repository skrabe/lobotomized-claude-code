<!--
name: 'Data: Sandbox excludedCommands setting'
description: >-
  Describes command-pattern sandbox exclusions, requiring every pipeline or
  chain component to match while keeping complex calls sandboxed and preserving
  permission checks
ccVersion: 2.1.314
-->
Command patterns (Bash permission-rule syntax) for commands to run outside the sandbox. An entry takes a call out of the sandbox only when every command in the call matches an entry: in a Bash pipe or a chain such as `a && b`, each part needs its own match. Some calls stay sandboxed whatever the entries, such as one with a `cd`, a command substitution, or a redirect other than a file-descriptor duplication like `2>&1`, a heredoc included. A convenience, not a security boundary: excluded commands still go through the permission flow. Merged across settings sources. 
