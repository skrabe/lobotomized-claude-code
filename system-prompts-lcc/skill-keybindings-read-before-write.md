<!--
name: 'Skill: Keybindings read before write'
description: >-
  Keybindings skill instruction to read ~/.claude/keybindings.json before merging changes.
ccVersion: 2.1.178
-->

**Always read `~/.claude/keybindings.json` first** (it may not exist yet). Merge changes with existing bindings — never replace the entire file.
