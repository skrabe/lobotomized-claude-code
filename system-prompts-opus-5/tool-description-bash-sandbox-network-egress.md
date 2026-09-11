<!--
name: 'Tool Description: Bash Sandbox Network Egress'
description: >-
  Command-sandbox restriction that network egress goes through a filtering proxy
  and denials appear in a sandbox_violations block.
ccVersion: 2.1.268
variables:
  - TOOL_DESCRIPTION_BASH_SANDBOX_NETWORK_EGRESS_VAR_0
-->
Network egress goes through a filtering proxy. Attempt requests and read the error rather than predicting whether a host is reachable; denied connections are reported in a \`<sandbox_violations>\` block explaining the reason${TOOL_DESCRIPTION_BASH_SANDBOX_NETWORK_EGRESS_VAR_0?". In auto mode, list the hosts a command needs beyond that in its `allowed_domains` — a denied host named in the block goes there on the re-run":""}.
