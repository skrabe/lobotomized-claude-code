<!--
name: 'Tool Parameter: Artifact Auto Open'
description: >-
  Artifact auto_open param describing when a type_url-created Artifact opens
  (at_create vs after_first_write).
ccVersion: 2.1.247
variables:
  - TOOL_PARAMETER_ARTIFACT_AUTO_OPEN_VAR_0
-->
Only with \`type_url\` and no \`file_path\`: when the new Artifact opens for the user. Pass "after_first_write" when you will fill it right after creating it (${TOOL_PARAMETER_ARTIFACT_AUTO_OPEN_VAR_0?'a later "write_db", or a files publish to its url':"a later files publish to its url"}), so the user does not first see it empty — it then opens on that first write. Omit otherwise: it opens when created.
