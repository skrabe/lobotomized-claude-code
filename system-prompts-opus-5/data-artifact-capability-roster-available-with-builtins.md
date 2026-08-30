<!--
name: 'Data: Artifact capability roster available with builtins'
description: >-
  Artifact-capabilities skill fragment listing declareable names plus built-in
  capabilities that must not be passed in `capabilities`.
ccVersion: 2.1.251
variables:
  - DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_0
  - DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_1
  - DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_2
-->
**Available capabilities:** ${DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_0.length>0?`${DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_1(DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_0)} — the complete set of capability names you may declare; `:"none to declare for this user; "}built in on every page, called without declaring (never pass these in \`capabilities\`): ${DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_1(DATA_ARTIFACT_CAPABILITY_ROSTER_AVAILABLE_WITH_BUILTINS_VAR_2)}. Anything not listed is unavailable to this user.
