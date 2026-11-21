<!--
name: 'System Reminder: Parallel Write Agent Same Checkout'
description: >-
  Agent-prompt note injected when another write-capable agent is already running
  in this checkout, telling this agent not to clobber its edits.
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_PARALLEL_WRITE_AGENT_SAME_CHECKOUT_VAR_0
-->
Note: another write-capable agent is already running in this same working directory, and ${SYSTEM_REMINDER_PARALLEL_WRITE_AGENT_SAME_CHECKOUT_VAR_0}
