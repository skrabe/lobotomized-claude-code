<!--
name: Malformed output request metadata
description: Specifies the required output object request metadata fields and bounds.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_MALFORMED_METADATA_VAR_0
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_MALFORMED_METADATA_VAR_1
-->
${TOOL_RESULT_SERVED_TOOL_OUTPUT_MALFORMED_METADATA_VAR_0} was not run: _meta["${TOOL_RESULT_SERVED_TOOL_OUTPUT_MALFORMED_METADATA_VAR_1}"] must be exactly { versions, deny_rules_digest }. versions: up to 64 whole numbers. deny_rules_digest: the SHA-256 of JSON.stringify(deny_rules), for the deny_rules this server advertises, as 64 lower-case hex characters.
