<!--
name: 'Slash Command: /permissions cloud session has no panel'
description: >-
  Explains that a cloud session has no permissions panel, that rules come from
  .claude/settings.json and that auto mode rules cannot be set that way
ccVersion: 2.1.319
-->
This cloud session has no permissions panel. Its rules come from its settings files: in a session with one repository, ask Claude to edit .claude/settings.json, and commit it to the repository to keep it for later sessions. Auto mode rules can't be set that way: a cloud session doesn't read them from that file or from ~/.claude/settings.json on your machine. For what each session reads, see https://code.claude.com/docs/en/settings#settings-in-cloud-sessions
