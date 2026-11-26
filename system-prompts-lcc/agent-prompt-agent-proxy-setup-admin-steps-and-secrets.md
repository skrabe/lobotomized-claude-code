<!--
name: 'Agent prompt: agent proxy setup admin steps and secrets'
description: >-
  Notes VM/network/firewall steps are the admin's and forbids printing keys or
  secrets
ccVersion: 2.1.332
-->
The VM, network and firewall steps are the admin's, run from elsewhere. Never print or open the agent proxy key, a private key or a secret value. As the skill says, any script that reads a secret is run by the user in their own terminal.
