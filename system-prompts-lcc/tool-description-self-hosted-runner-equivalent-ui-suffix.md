<!--
name: 'Tool Description: Self-hosted runner equivalent-UI suffix'
description: >-
  Shared suffix concatenated onto every self-hosted-runner admin tool
  description, telling the model to surface the equivalent.ui Admin-UI path and
  that auth is handled out of band.
ccVersion: 2.1.331
-->

The result includes an `equivalent.ui` string with the Admin-UI path. Surface it to the operator so they can repeat the action without you.
Auth: handled internally via the operator's `claude auth login` OAuth session — secrets never enter the conversation.
