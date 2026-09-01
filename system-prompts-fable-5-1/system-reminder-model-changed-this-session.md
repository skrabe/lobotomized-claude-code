<!--
name: 'System Reminder: Model changed this session'
description: >-
  Injected when the session model is switched mid-conversation, telling the
  model its new identity
ccVersion: 2.1.187
variables:
  - MODEL_NAME
-->
<system-reminder>The model for this session has been changed to ${MODEL_NAME}. You are now running as ${MODEL_NAME}.</system-reminder>
