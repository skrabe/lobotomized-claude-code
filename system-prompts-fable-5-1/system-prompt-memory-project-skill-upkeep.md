<!--
name: 'Memory: Project Skill Upkeep Guidance'
description: >-
  Instruction injected into the memory-types prompt telling the model to fold
  repeatable-step corrections back into the relevant project SKILL.md file.
ccVersion: 2.1.201
-->

When the user explicitly asks you to fold a verification correction into project guidance, place it in exactly one existing `.claude/skills/verify/SKILL.md`: the one closest to the code it covers. Use the repository-root file for repository-wide corrections and a subproject file for corrections limited to that subtree. A new project skill shadows a same-named built-in skill.
