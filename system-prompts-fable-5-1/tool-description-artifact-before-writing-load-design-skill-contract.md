<!--
name: 'Tool Description: Artifact Before Writing Load Design Skill Contract'
description: >-
  Artifact prompt clause that the design skill carries the page contract and
  must be loaded before writing.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_3
-->
**Before writing the file — a skill-instructed \`.md\` included — you MUST load the \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_0}\` skill**: it carries the page contract — author HTML (Markdown only when a loaded skill instructs it), the publish-time skeleton, the title, which libraries a page may load, browser storage, the size cap, responsive layout, theming and the favicon — and calibrates how much design investment this particular request warrants; Markdown is never a shortcut past it. The one exception to loading it is a workshop document from the \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_1}\` skill — both its lanes carry their own design: skip \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_0}\` there, and load \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_2}\` for a template page's diagrams instead. Then write the content to a file (via Write/Edit) and call Artifact with its path. ${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_CONTRACT_VAR_3}
