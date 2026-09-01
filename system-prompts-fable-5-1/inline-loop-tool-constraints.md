<!--
name: 'Inline blob: loop tool constraints'
description: '/loop autonomous-mode tool constraints note.'
inlineBlobAnchor: "`\n\n\\*\\*Tool constraints for this run:\\*\\* Shell access"
inlineBlobKind: 'template'
injectionGate: '/loop autonomous run with read-only restriction'
ccVersion: '2.1.211'
shadows:
  - system-reminder-memory-consolidation-tool-constraints
-->


**Tool constraints for this run:** Shell access is restricted to read-only commands (`ls`, `find`, `grep`, `cat`, `stat`, `wc`, `head`, `tail`, and similar) plus deleting `.md` paths inside the memory directory; anything else that writes, redirects to a file, or modifies state is denied. Memories are immutable — delete the file and write a fresh one rather than editing in place.

Sessions since last consolidation (${c7}):
${x4}
