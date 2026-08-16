<!--
name: 'Slash Command: /cd — trust prompt declined, staying put'
description: >-
  Tells the model the user declined to trust the new directory so the session's
  working directory is unchanged, naming the directory still in effect.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_TRUST_DECLINED_STAYING_VAR_0
  - SLASH_COMMAND_CD_TRUST_DECLINED_STAYING_VAR_1
-->
Staying in ${SLASH_COMMAND_CD_TRUST_DECLINED_STAYING_VAR_0.bold(SLASH_COMMAND_CD_TRUST_DECLINED_STAYING_VAR_1())}
