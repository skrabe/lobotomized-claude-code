<!--
name: Artifact Publish No Connector Named In Session
description: >-
  Publish warning that a declared connector name matches nothing in this
  session, with closest-name spelling advice.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_NO_CONNECTOR_NAMED_IN_SESSION_VAR_0
-->
no connector in this session is named ${TOOL_RESULT_ARTIFACT_PUBLISH_NO_CONNECTOR_NAMED_IN_SESSION_VAR_0} — if the closest name is the one you meant, declare it with exactly that spelling; viewers' connectors are matched by name (ignoring at most letter case and separators), so a name none of them carries works for no viewer.
