<!--
name: 'Tool Result: Artifact Describe Type Create Steps'
description: >-
  describe_type how-to line: publish with type_url, a title and no files first
  (passing auto_open after_first_write when filling next), then fill via store
  or data files.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_CREATE_STEPS_VAR_0
  - TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_CREATE_STEPS_VAR_1
-->
To start from it: publish with \`type_url\`: ${TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_CREATE_STEPS_VAR_0(TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_CREATE_STEPS_VAR_1)}, a \`title\` (what the user called it, or a short descriptive name) and no files first (passing \`auto_open: "after_first_write"\` when your next step publishes files to it or writes its store, never for a type whose content you write through a connector, such as a Claude Docs document); the create result carries the new Artifact's \`url\` and the type's instructions, and says how to fill it — documents written to its own store, or data files published to that \`url\`.
