<!--
name: 'Data: PreCompact hook output cut notice'
description: >-
  Marks PreCompact hook output truncated at the character limit before it joins
  the compaction instructions
ccVersion: 2.1.314
variables:
  - DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_0
  - DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_1
  - DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_2
  - DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_3
-->
${DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_0(DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_1,DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_2)}

[PreCompact hook [${DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_3.command}] output cut: ${DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_1.length} characters is over the ${DATA_PRECOMPACT_HOOK_OUTPUT_CUT_NOTICE_VAR_2}-character limit]
