<!--
name: 'Inline blob: memory how to save team'
description: '## How to save memories — team variant, index branch (two-step save with the shared index)'
inlineBlobAnchor: 'skipIndex:[$\w]+,file:"memory to its own file in the chosen directory \(private or team[^"]*"\}\):'
inlineBlobKind: 'array'
injectionGate: 'memory enabled + team memory'
ccVersion: '2.1.318'
inlineBlobRawPassthrough: 'true'
-->
"## How to save memories","","Saving a memory is a two-step process:","","**Step 1** — write the memory to its own file in the chosen directory (private or team, per the type's scope guidance) using this frontmatter format:","",...wJt,"",`**Step 2** — add a pointer to that file in \`${Yf}\` in the private directory. The single \`${Yf}\` indexes both private and team memories — use a path like \`file.md\` for private memories and \`team/file.md\` for team memories. Each entry should be one line, under ~150 characters: \`- [Title](file.md) — one-line hook\`. It has no frontmatter. Never write memory content directly into \`${Yf}\`.`,"",`- \`${Yf}\` is loaded into your conversation context — lines after ${fN} will be truncated, so keep the index concise`,"- Use a 3-4 word filename describing what it's about. Don't prefix with the memory type (already in frontmatter); don't restate the body in the filename.","- Pack the maximum context worth persisting into the fewest words — dense facts, not narrative.",...Xn
