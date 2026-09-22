<!--
name: 'Inline blob: skill keybindings header'
description: 'keybindings-help skill: header / overview.'
inlineBlobAnchor: '[$\w]+=\["# Keybindings Skill",'
inlineBlobKind: 'array'
injectionGate: 'keybindings-help skill'
ccVersion: '2.1.138'
shadows:
  - skill-keybindings-read-before-write
-->

# Keybindings Skill

Create or modify `~/.claude/keybindings.json` to customize keyboard shortcuts.

## Read Before Write

Read `~/.claude/keybindings.json` first (it may not exist yet). Merge changes with existing bindings — never replace the entire file.

- Use Edit for modifications to existing files
- Use Write only if the file does not exist yet
