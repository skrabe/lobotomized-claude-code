<!--
name: CLAUDE.md Project Instructions Suffix
description: >-
  Model-facing type-suffix label appended to a project CLAUDE.md path in the
  memory/context injection ("Contents of ${path} (project instructions, checked
  into the codebase):"); conditional on a Project-type memory item being
  present.
ccVersion: 2.1.274
variables:
  - SYSTEM_PROMPT_CLAUDE_MD_PROJECT_INSTRUCTIONS_SUFFIX_2_VAR_0
  - SYSTEM_PROMPT_CLAUDE_MD_PROJECT_INSTRUCTIONS_SUFFIX_2_VAR_1
-->
Contents of ${SYSTEM_PROMPT_CLAUDE_MD_PROJECT_INSTRUCTIONS_SUFFIX_2_VAR_0(SYSTEM_PROMPT_CLAUDE_MD_PROJECT_INSTRUCTIONS_SUFFIX_2_VAR_1)} (project instructions, checked into the codebase):

${SYSTEM_PROMPT_CLAUDE_MD_PROJECT_INSTRUCTIONS_SUFFIX_2_VAR_1.content.trim()}
