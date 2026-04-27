<!--
name: 'Skill: /dream memory consolidation'
description: >-
  Skill definition for the /dream nightly housekeeping job that consolidates
  recent logs and transcripts into persistent memory topics, learnings, and a
  pruned MEMORY.md index
ccVersion: 2.1.119
-->
---
name: dream
description: Nightly reflection and consolidation. Runs overnight (1–5am local) via the scheduled task scaffold.
context: fork
---

This is a housekeeping job — you should not need to message the user unless you find something noteworthy.

Your memory files are located in \`{{MEMORY_ROOT}}\`. The rest of the paths in this file can be assumed to be relative to this path.


**Phase 1: Preparation**
- Review recent memories in \`logs/YYYY/MM/YYYY-MM-DD.md\`
- Review session transcripts from the day in \`sessions/YYYY/MM/YYYY-MM-DD.md\`
- Review what topics and lessons already exist to ensure that you are improving existing topics if they are already covered, rather than creating duplicates.


**Phase 2: Topics**
- Extract significant events, lessons, decisions, and insights into topics stored as top level markdown files \`<topic-slug>.md\` in this directory.
- Make sure to resolve any contradictions


**Phase 3: Rules & Learnings**
- Review for anything that happened during the day that was painful or inefficient.
    - for example, not being able to build a project or get a test to run
- Review for anything that resulted in the user getting frustrated.
- Record the learnings from these experiences into \`learnings/<learning-slug>.md\`


**Phase 4: Prioritization and Pruning**
- We need to keep \`MEMORY.md\` under 200 lines. 
- These need to be *the most important* things for you to understand in the future.
- If something is getting too long, consider only mentioning the gist of it and referencing a separate file (like a topic file) with the full explanation.
- Consider if anything needs to be *removed* as it is becoming "stale" and no longer as important as it once was.
- Consider if anything should be *added* that has recently become more important. 

---

*Remember* - all of these memory files are *for you*. This is to help you situate and orient yourself in the future, after session context has been lost. Use these memories to allow for you to be the best possible assistant you can be.
