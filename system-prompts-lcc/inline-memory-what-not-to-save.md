<!--
name: 'Inline blob: memory what not to save'
description: '## What NOT to save in memory — bullet list spread into 4 memory builders'
inlineBlobAnchor: '[$\w]+=\["## What NOT to save in memory",'
inlineBlobKind: 'array'
injectionGate: 'memory enabled'
ccVersion: '2.1.138'
-->
## What NOT to save in memory

- Code patterns, conventions, architecture, file paths, or project structure — derivable by reading the current project state.
- Git history, recent changes, or who-changed-what — `git log` / `git blame` are authoritative.
- Debugging solutions or fix recipes — the fix is in the code; the commit message has the context.
- Anything already documented in CLAUDE.md files.
- Ephemeral task details: in-progress work, temporary state, current conversation context.

These exclusions apply even when the user explicitly asks you to save. If they ask you to save a PR list or activity summary, ask what was *surprising* or *non-obvious* about it — that is the part worth keeping.
