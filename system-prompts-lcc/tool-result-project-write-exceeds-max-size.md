<!--
name: 'Tool Result: project_write exceeds project max size'
description: >-
  project_write refusal when the write would exceed the project's maximum
  knowledge size.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_PROJECT_WRITE_EXCEEDS_MAX_SIZE_VAR_0
  - TOOL_RESULT_PROJECT_WRITE_EXCEEDS_MAX_SIZE_VAR_1
-->
Write refused: this write (~${TOOL_RESULT_PROJECT_WRITE_EXCEEDS_MAX_SIZE_VAR_0} tokens) would exceed the project's maximum size (~${TOOL_RESULT_PROJECT_WRITE_EXCEEDS_MAX_SIZE_VAR_1.max_knowledge_size} tokens). Delete unused docs or split the content across smaller writes.
