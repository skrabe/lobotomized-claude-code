<!--
name: 'Tool Description: SendUserFile status guidance'
description: >-
  SendUserFile prompt telling the model to set status on every call, using
  proactive when initiating so it reaches the user's phone and normal when
  replying
ccVersion: 2.1.325
-->
Set `status` on every call. Use `proactive` when you're initiating — the user is away and you want this to reach their phone (build artifact ready, report generated). Use `normal` when replying to something the user just said.
