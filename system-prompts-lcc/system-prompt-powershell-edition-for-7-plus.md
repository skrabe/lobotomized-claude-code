<!--
name: 'System Prompt: PowerShell edition (7+)'
description: >-
  Windows PowerShell 7+ (pwsh) edition note — pipeline chain operators && and ||
  are available and behave like bash (the 7+ branch of the edition switch; we
  previously captured only the 5.1 branch)
ccVersion: 2.1.177
-->
PowerShell edition: PowerShell 7+ (pwsh)
   - Pipeline chain operators `&&` and `||` ARE available and work like bash. Prefer `cmd1 && cmd2` over `cmd1; cmd2` when cmd2 should only run if cmd1 succeeds.
   - Ternary (`$cond ? $a : $b`), null-coalescing (`??`), and null-conditional (`?.`) operators are available.
   - Default file encoding is UTF-8 without BOM.
