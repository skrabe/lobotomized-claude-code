<!--
name: 'Tool Result: PowerShell Windows sandbox policy refusal'
description: >-
  Returned from the PowerShell tool's validateInput (and thrown on call) when
  enterprise policy requires sandboxing but the command would not be sandboxed
  on Windows; delivered to the model as the tool's error result
ccVersion: 2.1.214
-->
Enterprise policy requires sandboxing, but this command would not be sandboxed on Windows: either the sandbox is unavailable, or the command matches a sandbox exclusion pattern only in part. Compound commands and commands with shell metacharacters must run sandboxed even when a statement matches an exclusion.
