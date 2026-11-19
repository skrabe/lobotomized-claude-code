<!--
name: 'System Reminder: Low memory'
description: Resource watchdog reminder that little memory is available to this session
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_LOW_MEMORY_VAR_0
  - SYSTEM_REMINDER_LOW_MEMORY_VAR_1
  - SYSTEM_REMINDER_LOW_MEMORY_VAR_2
-->
Low memory: ${SYSTEM_REMINDER_LOW_MEMORY_VAR_0(SYSTEM_REMINDER_LOW_MEMORY_VAR_1.availableBytes)} was available to this session at ${new SYSTEM_REMINDER_LOW_MEMORY_VAR_2().toISOString().slice(11,16)} UTC${SYSTEM_REMINDER_LOW_MEMORY_VAR_1.limitedByCgroup?`, counting its ${SYSTEM_REMINDER_LOW_MEMORY_VAR_0(SYSTEM_REMINDER_LOW_MEMORY_VAR_1.totalBytes)} container limit. It may have changed since. \`free\` does not show that limit; the memory files under /sys/fs/cgroup do.`:". It may have changed since."}
