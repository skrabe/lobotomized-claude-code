<!--
name: 'Tool whenToUse: Artifact check addon'
description: >-
  Deferred-tool listing line telling Claude to check a page before claiming it
  works, noting an empty result may mean nobody opened it yet.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_ARTIFACT_CHECK_VAR_0
-->
When you are about to say that a page made for ${TOOL_WHEN_TO_USE_ARTIFACT_CHECK_VAR_0} works or looks right, use it to check first; an empty result can mean nobody has opened this version yet, not that the page works.
