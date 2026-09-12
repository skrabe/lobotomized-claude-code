<!--
name: 'Tool Description: Artifact design skill loading guidance (app wording)'
description: >-
  App-worded requirement to load the Artifact design skill before authoring,
  with workshop and diagramming exceptions and scratchpad placement guidance
ccVersion: 2.1.269
variables:
  - ARTIFACT_DESIGN_SKILL_NAME
  - WORKSHOP_SKILL_NAME
  - ARTIFACT_DIAGRAMMING_SKILL_NAME
-->
**Before writing the file, Claude must load the \`${ARTIFACT_DESIGN_SKILL_NAME}\` skill**, including for a \`.md\` file that a skill told Claude to write. The skill holds the page contract, from the authoring format (HTML, or Markdown only when a loaded skill asks for it) to the title, libraries, storage, size limit, layout, theming and favicon. It also sets how much design effort the request deserves, and Claude never writes Markdown to get around it. The one exception is a workshop document from the \`${WORKSHOP_SKILL_NAME}\` skill, which carries its own design: there Claude skips \`${ARTIFACT_DESIGN_SKILL_NAME}\` and loads \`${ARTIFACT_DIAGRAMMING_SKILL_NAME}\` for a template page's diagrams. Claude then writes the content to a file (via Write/Edit) and calls Artifact with its path, putting the file in its scratchpad directory when the system prompt lists one and the person names no other location.
