<!--
name: 'Tool Result: claude.ai skills sandbox refusal'
description: >-
  Note in the enabled claude.ai skills list result explaining that skills and
  plugins could not load because the sandboxed session uses a borrowed token
  with restricted network access
ccVersion: 2.1.325
-->
Couldn't load skills and plugins from your claude.ai account, so they may be missing from this session. Nothing in your account was changed. This session runs in a sandbox with restricted network access and is signed in with a token that isn't its own. If you supplied that token, remove it so the session uses its own sign-in. Otherwise, run Claude Code outside the sandbox or in one with unrestricted network access.
