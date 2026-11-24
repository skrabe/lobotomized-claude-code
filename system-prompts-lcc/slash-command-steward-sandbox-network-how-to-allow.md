<!--
name: 'Slash Command: Steward sandbox network how to allow'
description: >-
  How to let the watch start by editing sandbox.network
  deniedDomains/allowedDomains
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_0
  - SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_1
  - SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_2
  - SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_3
-->
 To let it start, ${[...SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_0.length>0?[`take ${SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_1(SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_0,"and")} off sandbox.network.deniedDomains in your settings`]:[],...SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_2.length>0?[`add ${SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_1(SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_2,"and")} to sandbox.network.allowedDomains in your user settings`]:[]].join(" and ")}, then run ${SLASH_COMMAND_STEWARD_SANDBOX_NETWORK_HOW_TO_ALLOW_VAR_3} again.
