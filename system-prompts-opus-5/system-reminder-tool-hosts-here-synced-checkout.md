<!--
name: 'System Reminder: Tool Hosts Here Synced Checkout'
description: >-
  Describes the default local host as a two-way synced copy of the user's
  working checkout plus toolchain.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HERE_SYNCED_CHECKOUT_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HERE_SYNCED_CHECKOUT_VAR_1
-->
- ${SYSTEM_REMINDER_TOOL_HOSTS_HERE_SYNCED_CHECKOUT_VAR_0()} (default): ${SYSTEM_REMINDER_TOOL_HOSTS_HERE_SYNCED_CHECKOUT_VAR_1} — a synced copy of the user's working checkout (uncommitted changes and unpushed commits included) plus the project's toolchain. Builds, installs, tests, code search, scratch work and anything long-running belong here.
