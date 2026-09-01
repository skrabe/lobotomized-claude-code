<!--
name: 'Inline blob: tool-usage "Prefer dedicated tools"'
description: >-
  Entry 1 of the inline tool-usage array. Tells the model to reach for dedicated
  tools (Read/Edit/Write) before Bash.
inlineBlobAnchor: '`Prefer dedicated tools over \$\{[$\w]+\} when one fits'
inlineBlobKind: template
injectionGate: always on (Bash tool loaded)
ccVersion: 2.1.141
-->

Prefer dedicated tools over ${O} when one fits (${T}) — reserve ${O} for shell-only operations.
