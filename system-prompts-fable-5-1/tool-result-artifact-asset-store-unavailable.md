<!--
name: Asset call failed — store unavailable
description: >-
  Artifact asset error arm for a store_unavailable code, defaulting to a
  retry-once-after-a-short-wait message.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_STORE_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_STORE_UNAVAILABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_STORE_UNAVAILABLE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_ASSET_STORE_UNAVAILABLE_VAR_0}: ${TOOL_RESULT_ARTIFACT_ASSET_STORE_UNAVAILABLE_VAR_1??`the asset store is unavailable right now — retry once after a short wait${TOOL_RESULT_ARTIFACT_ASSET_STORE_UNAVAILABLE_VAR_2==="upload"?" (an upload that timed out upstream may already be stored; a duplicate costs only quota)":""}`}
