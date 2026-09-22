<!--
name: 'Slash Command: /config Consent-Gated Key Rejected'
description: >-
  Message emitted when /config key=value tries to enable a consent-gated
  setting, telling the user to open the /config panel; returned as the command's
  text output and injected as <local-command-stdout>.
ccVersion: 2.1.211
variables:
  - SLASH_COMMAND_CONFIG_CONSENT_GATED_KEY_VALUE_REJECTED_VAR_0
-->
${SLASH_COMMAND_CONFIG_CONSENT_GATED_KEY_VALUE_REJECTED_VAR_0} can't be enabled with key=value — open /config to change it from the panel.
