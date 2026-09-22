<!--
name: Invoke-Item runs default handler
description: >-
  PowerShell command-safety approval reason surfaced to the model warning
  Invoke-Item can execute arbitrary code.
ccVersion: 2.1.206
-->
Invoke-Item opens files with the default handler (ShellExecute). On executable files this runs arbitrary code.
