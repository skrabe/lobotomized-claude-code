<!--
name: 'Skill: /send-to-project quoted context sources'
description: >-
  Explains what the folder's context quotes and to work from it (and the
  conversation) without running git or reading other files
ccVersion: 2.1.314
variables:
  - SKILL_SEND_TO_PROJECT_QUOTED_CONTEXT_SOURCES_VAR_0
-->
The folder’s context quotes what the CLI read from this computer when the command ran: git metadata, file excerpts${SKILL_SEND_TO_PROJECT_QUOTED_CONTEXT_SOURCES_VAR_0?"":" and condensed transcripts of the user’s own past sessions here (what they typed and what Claude answered; no tool or command output)"}, between two marker lines that it names. Work from it${SKILL_SEND_TO_PROJECT_QUOTED_CONTEXT_SOURCES_VAR_0?" and the conversation above":" alone"}: there is no need to run git, open transcripts or read other files for this.
