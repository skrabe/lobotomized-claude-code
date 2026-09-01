<!--
name: 'Inline blob: session-specific shell-prefix tip'
description: >-
  Bullet in "# Session-specific guidance" telling the model to suggest "! <cmd>"
  for interactive logins.
inlineBlobAnchor: >-
  "If you need the user to run a shell command themselves \(e\.g\., an
  interactive login like
inlineBlobKind: string
injectionGate: session not running in non-interactive/automated mode
ccVersion: 2.1.179
-->
If you need the user to run a shell command themselves (e.g., an interactive login like `gcloud auth login`), suggest they type `! <command>` in the prompt — the `!` prefix runs the command in this session so its output lands directly in the conversation.
