<!--
name: 'Tool Description: Artifact Separate Tools Load When Needed'
description: >-
  Separate-tools paragraph telling Claude to load each addon tool when needed,
  including deferred-tool loading.
ccVersion: 2.1.269
variables:
  - TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0
-->
**Separate tools**: Claude handles ${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0.length<=2?TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0.join(" and "):`${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0.slice(0,-1).join(", ")}, and ${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0.at(-1)}`}. Claude loads ${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0.length===1?"that tool":TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0.length===2?"either tool":"each of these tools"} when it needs it, and if ${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_WHEN_NEEDED_VAR_0.length===1?"it":"one"} appears only as a deferred tool's name, Claude loads it the way this session loads deferred tools before calling it.
