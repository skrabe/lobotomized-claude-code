<!--
name: 'API Error: Gateway did not accept sign-in'
description: >-
  Clause appended to the gateway-refused API error when the organization gateway
  did not accept the user's sign-in, with the sign-in-again step slot.
ccVersion: 2.1.330
variables:
  - DATA_API_ERROR_GATEWAY_SIGN_IN_NOT_ACCEPTED_VAR_0
-->
 · it did not accept your sign-in to it${DATA_API_ERROR_GATEWAY_SIGN_IN_NOT_ACCEPTED_VAR_0.signInAgainStep()??": /login can't offer that sign-in here, so ask your administrator"}
