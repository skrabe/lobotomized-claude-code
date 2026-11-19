<!--
name: 'Tool result: PowerShell Get-Module manifest ask'
description: >-
  Permission ask message that Get-Module can load a manifest that runs commands,
  so approve only trusted modules
ccVersion: 2.1.328
-->
This command may run Get-Module, which can load a module manifest, and a manifest can run any command. Approve only if you trust every module or path it names or receives from the pipeline
