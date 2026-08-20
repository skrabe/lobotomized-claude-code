<!--
name: 'Data: Artifact Live-Subscription Arm-Failed Event'
description: >-
  Task-notification <event> telling the model a live artifact watch did not arm
  and this session is not watching it.
ccVersion: 2.1.237
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_3
-->

<event>${DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_0(`The live subscription for ${DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_1.url} did not arm — ${DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_2}. This session is NOT watching it and will not hear when it is republished; ${DATA_TASK_NOTIFICATION_ARTIFACT_LIVE_SUBSCRIPTION_ARM_FAILED_VAR_3}, and do not claim to be watching it meanwhile.`)}</event>
