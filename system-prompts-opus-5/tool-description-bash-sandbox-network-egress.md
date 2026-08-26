<!--
name: 'Tool Description: Bash Sandbox Network Egress'
description: >-
  Command-sandbox restriction that network egress goes through a filtering proxy
  and denials appear in a sandbox_violations block.
ccVersion: 2.1.246
-->
Network egress goes through a filtering proxy. Attempt requests and read the error rather than predicting whether a host is reachable; denied connections are reported in a `<sandbox_violations>` block explaining the reason.
