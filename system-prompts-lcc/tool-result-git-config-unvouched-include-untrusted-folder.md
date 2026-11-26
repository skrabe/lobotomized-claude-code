<!--
name: 'Git config: include in untrusted folder'
description: >-
  Reason that an untrusted folder's git config includes another file, so what
  git would load can't be determined.
ccVersion: 2.1.332
-->
this folder isn't trusted here, and the repository's git config includes another file (include.path), isn't a plain file or couldn't be checked, so Claude Code can't tell what git would load (if you trust the folder, reload the window or use Review trust in the Claude Code panel if it shows, then start a new session; outside VS Code, start Claude Code without --ignore-persisted-trust or CLAUDE_CODE_IGNORE_PERSISTED_TRUST)
