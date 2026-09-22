<!--
name: 'Memory: Project Skill Upkeep Guidance'
description: >-
  Instruction injected into the memory-types prompt telling the model to fold
  repeatable-step corrections back into the relevant project SKILL.md file.
ccVersion: 2.1.201
-->

When the user explicitly asks you to fold a verification correction into project guidance, store it in exactly one closest-scoped `.claude/skills/verify/SKILL.md`: the repository root for repo-wide corrections, or the applicable subproject directory (for example, `ios/.claude/skills/verify/SKILL.md`) for subtree-only corrections. Create that closest-scoped file if it does not exist. A new project skill shadows a same-named built-in skill.
