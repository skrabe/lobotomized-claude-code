<!--
name: 'Data: Organization sign-in new session required refusal'
description: >-
  Refuses a request after an organization sign-in that only a new session takes
  up and says how to continue
ccVersion: 2.1.330
variables:
  - DATA_ORGANIZATION_SIGN_IN_NEW_SESSION_REQUIRED_REFUSAL_VAR_0
-->
Claude Code did not send this request. After a sign-in to your organization, only a new session sends requests. To continue, ${DATA_ORGANIZATION_SIGN_IN_NEW_SESSION_REQUIRED_REFUSAL_VAR_0?"open the conversation again from Session history":"exit, then run `claude`"}.
