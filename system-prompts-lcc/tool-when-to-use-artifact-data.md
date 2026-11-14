<!--
name: 'Tool whenToUse: Artifact data addon'
description: >-
  Deferred-tool listing line telling Claude when to use the artifact
  shared-database (data) tool and to use the artifact tool for the page itself.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_ARTIFACT_DATA_VAR_0
-->
When you are about to read or change documents in a published artifact's shared database, or look up the display name for a "u_" person id, use it; to publish or read the page itself, use ${TOOL_WHEN_TO_USE_ARTIFACT_DATA_VAR_0}.
