<!--
name: 'API Error: Gateway Not Named In Managed Settings'
description: >-
  Refused-request error saying the organization's gateway is not named in
  managed settings (forceLoginGatewayUrl), with a reason slot; thrown as the
  API-route refusal the model sees.
ccVersion: 2.1.330
variables:
  - DATA_API_ERROR_GATEWAY_NOT_NAMED_IN_MANAGED_SETTINGS_VAR_0
-->
Claude Code did not send this request. Your organization sends Claude Code's requests through its gateway, but this computer's managed settings do not name that gateway, so Claude Code does not sign in to it here. ${DATA_API_ERROR_GATEWAY_NOT_NAMED_IN_MANAGED_SETTINGS_VAR_0}. Ask your IT administrator to name the gateway in this computer's managed settings (forceLoginGatewayUrl), then start Claude Code again.
