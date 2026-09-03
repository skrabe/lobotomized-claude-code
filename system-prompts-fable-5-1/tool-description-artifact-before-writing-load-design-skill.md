<!--
name: 'Tool Description: Artifact Before Writing Load Design Skill'
description: >-
  Artifact prompt clause requiring the design skill be loaded before writing a
  skill-instructed markdown page.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_VAR_2
-->
**Before writing the file — a skill-instructed \`.md\` included — you MUST load the \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_VAR_0}\` skill** to calibrate how much design investment this particular request warrants. Format is not part of that decision — the Format rule above settles it, and Markdown is never a shortcut past the design pass. The one exception to loading it is a workshop document from the \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_VAR_1}\` skill — both its lanes carry their own design: skip \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_VAR_0}\` there, and load \`${TOOL_DESCRIPTION_ARTIFACT_BEFORE_WRITING_LOAD_DESIGN_SKILL_VAR_2}\` for a template page's diagrams instead. Then write the content to a file (via Write/Edit) and call Artifact with its path.
