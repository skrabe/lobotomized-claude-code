<!--
name: 'Tool Parameter: Artifact share people'
description: >-
  Artifact tool input-schema description of the share action's people parameter:
  names or work emails as hints (1-${_7t} entries), which the host resolves and
  the user confirms on the card.
ccVersion: 2.1.286
variables:
  - TOOL_PARAMETER_ARTIFACT_SHARE_PEOPLE_VAR_0
-->
share with mode "people" only: who to share with, as the user described them — names or work emails, 1-${TOOL_PARAMETER_ARTIFACT_SHARE_PEOPLE_VAR_0} entries. Hints, not grants: the host resolves them to organization members and the user confirms or edits the list on the card. Omit for mode "org".
