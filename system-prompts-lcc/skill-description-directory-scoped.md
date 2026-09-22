<!--
name: Directory-scoped skill description suffix
description: >-
  Augmented skill description injected so the model knows the skill is from a
  directory .claude/skills and applies to files under that directory.
ccVersion: 2.1.206
variables:
  - SKILL_DESCRIPTION_DIRECTORY_SCOPED_VAR_0
  - SKILL_DESCRIPTION_DIRECTORY_SCOPED_VAR_1
-->
${SKILL_DESCRIPTION_DIRECTORY_SCOPED_VAR_0.description} (from ${SKILL_DESCRIPTION_DIRECTORY_SCOPED_VAR_1}/.claude/skills — applies when working on files under ${SKILL_DESCRIPTION_DIRECTORY_SCOPED_VAR_1}/)
