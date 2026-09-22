<!--
name: Artifact Read Asset Out Dir No Consent Surface
description: >-
  checkPermissions deny for read_asset out_dir outside working folders when no
  one can answer the prompt.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_READ_ASSET_OUT_DIR_NO_CONSENT_SURFACE_VAR_0
-->
read_asset saves outside this session’s working folders and scratchpad only with the user’s approval, and no one can answer the prompt in this session — ${TOOL_RESULT_ARTIFACT_READ_ASSET_OUT_DIR_NO_CONSENT_SURFACE_VAR_0===void 0||TOOL_RESULT_ARTIFACT_READ_ASSET_OUT_DIR_NO_CONSENT_SURFACE_VAR_0===""?"this asset cannot be saved here; raise the read with the user in chat, or the user can run it where they can approve it.":"omit out_dir so the asset lands in this session’s scratchpad folder for the artifact (the working directory when the session has none), or raise it with the user in chat."}
