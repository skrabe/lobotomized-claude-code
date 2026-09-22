<!--
name: 'Inline blob: tool-usage "Use TaskCreate to plan and track work"'
description: >-
  Entry 2 of the inline tool-usage array. REDUNDANT with
  tool-description-taskcreate (which is the source of truth). Recommended: empty
  body to suppress this duplicate. Note: empty body leaves an empty string in
  the array → produces a blank line in the rendered "# Using your tools"
  section.
inlineBlobAnchor: '`Use \$\{[$\w]+\} to plan and track work\. Mark each task completed'
inlineBlobKind: template
injectionGate: always on (TaskCreate tool loaded)
ccVersion: 2.1.141
-->

Use ${_} to plan and track work. Mark each task completed as soon as it's done; don't batch.
