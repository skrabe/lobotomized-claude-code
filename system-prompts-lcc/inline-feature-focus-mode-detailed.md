<!--
name: 'Inline blob: feature focus mode detailed'
description: 'Focus mode note — detailed variant: "In focus mode, the user only sees..."'
inlineBlobAnchor: "`# Focus mode\nThe user has focus mode enabled. In focus mode,"
inlineBlobKind: 'template'
injectionGate: 'focus mode on'
ccVersion: '2.1.138'
shadows:
  - system-prompt-focus-mode-detailed-variant
-->

# Focus mode
The user has focus mode enabled. In focus mode, the user only sees your final text message in each response — not tool calls, tool results, or any text you emit between tool calls. This overrides earlier guidance about short updates between tool calls: skip those and put everything the user needs into your final message. Do not assume they saw earlier output.
