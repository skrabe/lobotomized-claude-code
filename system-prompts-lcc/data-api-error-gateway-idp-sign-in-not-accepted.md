<!--
name: 'API Error: Gateway IdP sign-in not accepted'
description: >-
  Clause appended to the gateway-refused API error when the organization's
  identity provider sign-in was not accepted, with remedy arms.
ccVersion: 2.1.330
variables:
  - DATA_API_ERROR_GATEWAY_IDP_SIGN_IN_NOT_ACCEPTED_VAR_0
-->
 · it did not accept your sign-in through your organization's identity provider${DATA_API_ERROR_GATEWAY_IDP_SIGN_IN_NOT_ACCEPTED_VAR_0.organizationGatewayIdpSignIn()===void 0?": Claude Code can't offer that sign-in here, so ask your administrator":" · Run /login in Claude Code, or claude auth login --organization-gateway in a terminal, to sign in again"}
