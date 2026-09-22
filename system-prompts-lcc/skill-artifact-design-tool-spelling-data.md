<!--
name: 'Skill: Artifact Design Tool Spelling Data'
description: >-
  artifact-design skill substitution mapping Artifact read_db/write_db onto the
  dedicated db tool's db_op actions.
ccVersion: 2.1.265
variables:
  - SKILL_ARTIFACT_DESIGN_TOOL_SPELLING_DATA_VAR_0
  - SKILL_ARTIFACT_DESIGN_TOOL_SPELLING_DATA_VAR_1
  - SKILL_ARTIFACT_DESIGN_TOOL_SPELLING_DATA_VAR_2
-->
the \`${SKILL_ARTIFACT_DESIGN_TOOL_SPELLING_DATA_VAR_0}\` tool's \`action: "read_db"\` / \`"write_db"\` with a \`db_op\` are the \`${SKILL_ARTIFACT_DESIGN_TOOL_SPELLING_DATA_VAR_1}\` tool, whose \`action\` is that \`db_op\` ("get", "list", "query", "set", "update",${SKILL_ARTIFACT_DESIGN_TOOL_SPELLING_DATA_VAR_2()?' "str_replace",':""} "delete", "batch") with the other fields unchanged
