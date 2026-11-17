<!--
name: 'Tool Result: PowerShell code-loading keywords unchecked'
description: >-
  Permission message when a PowerShell command contains using module/assembly,
  #requires or Import-DscResource, so it was not parsed and permission rules
  could not be fully checked.
ccVersion: 2.1.326
-->
PowerShell can load code while reading `using module`, `using assembly`, `#requires` or `Import-DscResource`, so Claude Code did not let it read this command and could not fully check your permission rules. The words may be harmless, such as text in a string.
