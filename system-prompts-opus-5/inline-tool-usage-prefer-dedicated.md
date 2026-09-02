<!--
name: 'Inline blob: tool-usage "Prefer dedicated tools"'
description: >-
  Entry 1 of the inline tool-usage array. Tells the model to reach for dedicated
  tools (Read/Edit/Write) before Bash. Emptied 2026-09-02: the set is
  bash-first (system-prompt-bash-first-tool-preference), and the same literal
  is suppressed under system-prompt-prefer-dedicated-tools-default-cli; two
  overrides of one literal must agree.
inlineBlobAnchor: '`Prefer dedicated tools over \$\{[$\w]+\} when one fits'
inlineBlobKind: template
injectionGate: always on (Bash tool loaded)
ccVersion: 2.1.141
-->
