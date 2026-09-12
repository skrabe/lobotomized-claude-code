<!--
name: 'Tool Description: Artifact watching publish result (app wording)'
description: >-
  App-worded watching clause that each publish result says whether this session
  now watches the artifact, and that Claude must not claim a watch the result
  did not confirm.
ccVersion: 2.1.269
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_PUBLISH_RESULT_APP_WORDING_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_PUBLISH_RESULT_APP_WORDING_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_PUBLISH_RESULT_APP_WORDING_VAR_2
-->
**Watching**: each publish result says whether this session now watches that artifact, for republishes from elsewhere${TOOL_DESCRIPTION_ARTIFACT_WATCHING_PUBLISH_RESULT_APP_WORDING_VAR_0?" and for comments sent to Claude":""}. Claude never claims a watch that a result did not confirm.${TOOL_DESCRIPTION_ARTIFACT_WATCHING_PUBLISH_RESULT_APP_WORDING_VAR_1}${TOOL_DESCRIPTION_ARTIFACT_WATCHING_PUBLISH_RESULT_APP_WORDING_VAR_2}
