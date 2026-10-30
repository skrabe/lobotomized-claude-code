<!--
name: 'Send to Project: Unused claude.ai connectors'
description: >-
  Line in the /send-to-project folder facts listing claude.ai connectors that
  are connected but not used in the read sessions.
ccVersion: 2.1.314
variables:
  - DATA_SEND_TO_PROJECT_UNUSED_CLAUDEAI_CONNECTORS_VAR_0
-->
Connected on claude.ai but not used in these sessions: ${DATA_SEND_TO_PROJECT_UNUSED_CLAUDEAI_CONNECTORS_VAR_0.otherConnectors.join(", ")}${DATA_SEND_TO_PROJECT_UNUSED_CLAUDEAI_CONNECTORS_VAR_0.moreConnectors>0?` (+${DATA_SEND_TO_PROJECT_UNUSED_CLAUDEAI_CONNECTORS_VAR_0.moreConnectors} more)`:""}.
