<!--
name: 'Inline blob: memory directory intro (noteam)'
description: >-
  Single-line intro pointing at the memory directory. Followed by a "should not
  require mkdir" instruction interpolated via the second variable.
inlineBlobAnchor: >-
  `You have a persistent, file-based memory system at \\`\$\{[$\w]+\}\\`\.
  \$\{[$\w]+\}`
inlineBlobKind: template
injectionGate: 'memory enabled, noteam mode'
ccVersion: 2.1.141
-->
You have a persistent, file-based memory system at \`${_}\`. ${C4H}
