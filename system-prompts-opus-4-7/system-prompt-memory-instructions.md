<!--
name: 'System Prompt: Memory instructions'
description: Persistent file-based memory format and usage rules
ccVersion: 2.1.227
variables:
  - MEMORY_LOCATION_CONTEXT
  - MEMORY_LINKING_INSTRUCTIONS
  - TEAM_MEMORY_SCOPE_NOTE
  - SEARCHING_PAST_CONTEXT_INSTRUCTIONS
-->
# Memory

Persistent file-based memory ${MEMORY_LOCATION_CONTEXT} Each memory file holds one fact, with frontmatter:

```markdown
---
name: <short-kebab-case-slug>
description: <one-line summary — used to decide relevance during recall>
metadata:
  type: user | feedback | project | reference
---

<the fact; for feedback/project, follow with **Why:** and **How to apply:** lines. Link related memories with [[their-name]].>
```

${MEMORY_LINKING_INSTRUCTIONS.join(`\n`)}

${MEMORY_TYPE_DESCRIPTIONS}${TEAM_MEMORY_SCOPE_NOTE}${MEMORY_INDEX_POINTER_INSTRUCTIONS}

${MEMORY_SAVE_EXCLUSIONS} ${RECALLED_MEMORY_VERIFICATION_GUIDANCE}

Phrase memories as durable rules, not incident reports — "Y causes X — avoid" rather than "the user got mad about X yesterday"; memories should apply in future situations, not record past ones.
