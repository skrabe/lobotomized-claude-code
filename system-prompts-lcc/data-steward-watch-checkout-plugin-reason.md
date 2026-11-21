<!--
name: 'Data: Steward watch checkout plugin reason'
description: >-
  Why a /steward watch is limited: a plugin the checkout holds, switches on, or
  declares a marketplace for
ccVersion: 2.1.330
variables:
  - DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_REASON_VAR_0
  - DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_REASON_VAR_1
-->
a plugin that this checkout holds, switches on, or declares a marketplace for${/^[\w.-]{1,60}@[\w.-]{1,60}$/.test(DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_REASON_VAR_0)?` (${DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_REASON_VAR_0})`:""} ${DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_REASON_VAR_1}
