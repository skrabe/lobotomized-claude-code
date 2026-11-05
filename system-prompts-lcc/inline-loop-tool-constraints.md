<!--
name: 'Inline blob: loop tool constraints'
description: '/loop autonomous-mode tool constraints note.'
inlineBlobAnchor: "`\n\n\\*\\*Tool constraints for this run:\\*\\* Shell access"
inlineBlobKind: 'template'
injectionGate: '/loop autonomous run with read-only restriction'
ccVersion: '2.1.318'
shadows:
  - system-reminder-memory-consolidation-tool-constraints
-->


**Tool constraints for this run:** Shell access is restricted to read-only commands (`ls`, `find`, `grep`, `cat`, `stat`, `wc`, `head`, `tail`, and similar) plus deleting `.md` files inside the memory directory (outside protected subdirectories like `.git` or `agents`; `rm` takes no flags except `-f`); anything else that writes, redirects to a file, or modifies state is denied.

Sessions since last consolidation (${c7}):
${x4}
