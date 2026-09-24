<!--
name: 'Tool Description: Bash sandbox local port binding blocked (user can allow)'
description: >-
  Bash sandbox guidance: an EPERM on binding a local port means local binding is
  off, so tell the user they can enable sandbox.network.allowLocalBinding (with
  exclude or ! options), and leave that decision to them.
ccVersion: 2.1.281
variables:
  - TOOL_DESCRIPTION_BASH_SANDBOX_LOCAL_BINDING_BLOCKED_USER_SETTING_VAR_0
-->
If a command fails to bind or listen on a local port with "Operation not permitted" (EPERM), local port binding is off in this sandbox. Tell the user they can allow it with \`sandbox.network.allowLocalBinding: true\` in their settings (it applies without a restart)${TOOL_DESCRIPTION_BASH_SANDBOX_LOCAL_BINDING_BLOCKED_USER_SETTING_VAR_0}.
