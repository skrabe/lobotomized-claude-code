<!--
name: 'Tool Result: Artifact publish unasked shape refused'
description: >-
  Artifact publish tool error when a publish made without asking does more than
  create a new artifact, saying nothing was published and later publishes need
  the usual permission check
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_UNASKED_SHAPE_REFUSED_VAR_0
-->
Nothing was published: a publish made without asking may only create a new artifact, naming no url and setting no capabilities, contract, force, file removals or live files, but this one ${TOOL_RESULT_ARTIFACT_PUBLISH_UNASKED_SHAPE_REFUSED_VAR_0}. Every publish in this session now goes through the usual permission check, which may need a person's approval.
