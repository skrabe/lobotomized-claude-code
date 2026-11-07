<!--
name: 'Skill: Claude API sign-in without a browser'
description: >-
  Claude API skill bullet for sign-in over SSH with --no-browser and for web
  sessions setting ANTHROPIC_API_KEY in a cloud environment
ccVersion: 2.1.319
-->
- **No browser on this machine:** over SSH they run `ant auth login --no-browser` in a terminal of their own on that host (`!` and your own commands get no keyboard input). Where they have only this chat (Claude Code on the web, `CLAUDE_CODE_REMOTE=true`), don't start a login: they set `ANTHROPIC_API_KEY` in the settings of a cloud environment only they use, then start a new session.
