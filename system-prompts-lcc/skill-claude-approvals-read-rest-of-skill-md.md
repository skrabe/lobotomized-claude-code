<!--
name: 'Claude Approvals skill: read rest of SKILL.md'
description: >-
  Note telling the model the SKILL.md opening was shown and to read the rest
  from a line number before editing a policy file.
ccVersion: 2.1.331
variables:
  - SKILL_CLAUDE_APPROVALS_READ_REST_OF_SKILL_MD_VAR_0
  - SKILL_CLAUDE_APPROVALS_READ_REST_OF_SKILL_MD_VAR_1
  - SKILL_CLAUDE_APPROVALS_READ_REST_OF_SKILL_MD_VAR_2
-->
This is the opening of \`SKILL.md\`. The rest of that file, from "Workflow" on, holds the steps and recipes of an edit: it is what the table above calls "the rest of this file". Before you create or change a policy file, read \`SKILL.md\` in the base directory from line ${SKILL_CLAUDE_APPROVALS_READ_REST_OF_SKILL_MD_VAR_0(SKILL_CLAUDE_APPROVALS_READ_REST_OF_SKILL_MD_VAR_1.slice(0,SKILL_CLAUDE_APPROVALS_READ_REST_OF_SKILL_MD_VAR_1.search(SKILL_CLAUDE_APPROVALS_READ_REST_OF_SKILL_MD_VAR_2)),`
`)+2} to its end.
