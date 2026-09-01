<!--
name: 'Inline blob: skill keybindings keystroke syntax'
description: 'keybindings-help skill: keystroke syntax.'
inlineBlobAnchor: '[$\w]+=\["## Keystroke Syntax",'
inlineBlobKind: 'array'
injectionGate: 'keybindings-help skill'
ccVersion: '2.1.138'
-->

## Keystroke Syntax

**Modifiers** (combine with `+`):
- `ctrl` (alias: `control`)
- `alt` (aliases: `opt`, `option`) — note: `alt` and `meta` are identical in terminals
- `shift`
- `meta` (aliases: `cmd`, `command`)

**Special keys**: `escape`/`esc`, `enter`/`return`, `tab`, `space`, `backspace`, `delete`, `up`, `down`, `left`, `right`

**Chords**: Space-separated keystrokes, e.g. `ctrl+k ctrl+s` (1-second timeout between keystrokes)

**Examples**: `ctrl+shift+p`, `alt+enter`, `ctrl+k ctrl+n`
