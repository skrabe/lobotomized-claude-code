<!--
name: 'Skill: Keybindings validation cause not a modifier'
description: >-
  Keybindings skill validation table cause cell: a non-modifier before the key
  is dropped, so the binding applies to a different keystroke.
ccVersion: 2.1.325
-->
Error: `X` comes before the key in `Y` but is not a modifier (a typo such as `ctl` for `ctrl`, or two keys joined with `+` instead of a space), so the binding is ignored and every key keeps its current action
