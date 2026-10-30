<!--
name: 'Tool Description: Monitor timeout likely stopped after reply'
description: >-
  Monitor tool description timeout note (K_ sessions): expiry or kill on
  timeout, plus that any monitor is likely stopped a few minutes after the reply
  without notice.
ccVersion: 2.1.314
variables:
  - TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_0
  - TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_1
  - TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_2
  - TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_3
-->
${TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_0()?`Every monitor expires after \`timeout_ms\` (default ${TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_1(TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_2)}, at most ${TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_1(TOOL_DESCRIPTION_MONITOR_TIMEOUT_LIKELY_STOPPED_AFTER_REPLY_VAR_3())}): it is killed and you get one notice with the event count.`:"Timeout → killed."} Any monitor is also likely stopped a few minutes after your reply, and you may hear nothing of that until the user writes again.
