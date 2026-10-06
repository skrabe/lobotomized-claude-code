<!--
name: 'Tool Result: sandbox invalid IP or CIDR range'
description: >-
  Error thrown while building the sandbox network policy when a configured
  denied/allowed address entry is not a valid IP address or CIDR range; surfaces
  as a Bash tool error result.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SANDBOX_INVALID_IP_OR_CIDR_RANGE_VAR_0
  - TOOL_RESULT_SANDBOX_INVALID_IP_OR_CIDR_RANGE_VAR_1
-->
Invalid IP address or CIDR range: ${TOOL_RESULT_SANDBOX_INVALID_IP_OR_CIDR_RANGE_VAR_0.stringify(TOOL_RESULT_SANDBOX_INVALID_IP_OR_CIDR_RANGE_VAR_1)}
