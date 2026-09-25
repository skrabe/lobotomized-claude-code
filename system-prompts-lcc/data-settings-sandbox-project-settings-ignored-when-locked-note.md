<!--
name: 'Data: Settings sandbox project settings ignored when locked note'
description: >-
  Settings-schema describe fragment noting that project settings values are
  ignored when managed settings or --settings lock allowUnsandboxedCommands or
  allowManagedDomainsOnly
ccVersion: 2.1.282
-->
When managed settings or a --settings file set allowUnsandboxedCommands: false, or managed settings set network.allowManagedDomainsOnly: true, values from project settings (.claude/settings.json and .claude/settings.local.json) are ignored.
