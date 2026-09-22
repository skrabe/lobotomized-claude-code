<!--
name: 'Data: tui setting description'
description: >-
  Description of the `tui` setting in Claude Code's settings JSON schema. The
  model reads it through /update-config and settings validation errors; it is
  also shown to users in the settings help.
ccVersion: 2.1.276
-->
Terminal UI renderer. "fullscreen" uses the flicker-free alt-screen renderer with virtualized scrollback (equivalent to CLAUDE_CODE_NO_FLICKER=1). "default" uses the classic main-screen renderer.
