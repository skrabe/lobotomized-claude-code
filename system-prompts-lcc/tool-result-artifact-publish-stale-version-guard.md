<!--
name: 'Tool Result: Artifact publish stale version guard'
description: >-
  Artifact tool error when an earlier same-turn read returned only a
  summary/page data of a newer version.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_STALE_VERSION_GUARD_VAR_0
-->
A read earlier in this same turn recorded this artifact's newer live version but returned only ${TOOL_RESULT_ARTIFACT_PUBLISH_STALE_VERSION_GUARD_VAR_0==="summary"?"a summary of it":"its page data"}, not its source, so nothing was published. 
