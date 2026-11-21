<!--
name: 'API error: Bedrock token unused (region partition)'
description: >-
  Reason clause: managed settings set a region outside the organization's AWS
  partition, so the personal Bedrock key is set aside.
ccVersion: 2.1.330
variables:
  - DATA_API_ERROR_BEDROCK_TOKEN_UNUSED_REGION_PARTITION_REASON_VAR_0
-->
this computer's managed settings set ${DATA_API_ERROR_BEDROCK_TOKEN_UNUSED_REGION_PARTITION_REASON_VAR_0} to a region that Claude Code can't place in the same AWS partition (such as GovCloud) as your organization's region, and the key may belong to that region. Ask your IT administrator about it
