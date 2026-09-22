<!--
name: 'Data: Import Unmappable — Codex Permission Mode (Project Scope)'
description: >-
  Reason text for an unmappable Codex approval_policy at project scope;
  interpolated into the generated import-to-claude-code SKILL.md and into the
  /import preview prompt the model summarises.
ccVersion: 2.1.214
-->
Maps to `defaultMode: auto`, which repo-level settings cannot grant in Claude Code (and the ignored value would shadow your user-level permission mode). Adopt it in your user settings instead if you want it.
