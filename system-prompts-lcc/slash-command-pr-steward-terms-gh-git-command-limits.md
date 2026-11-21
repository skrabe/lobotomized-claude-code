<!--
name: 'Slash command: PR Steward terms gh and git limits'
description: >-
  Explains that gh and git commands are limited but file reads and Claude Code
  hooks are not
ccVersion: 2.1.330
-->
- Claude Code limits my gh and git commands to a short list, which stops a direct merge or force-push. It doesn't limit which files shell commands like cat or grep read. Inside your working folders they run without asking. It also doesn't stop your Claude Code hooks, which run without asking and may run a file I've edited.
