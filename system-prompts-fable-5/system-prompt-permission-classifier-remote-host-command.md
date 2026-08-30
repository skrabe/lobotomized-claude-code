<!--
name: 'Permission Classifier: Remote Host Command Prefix'
description: >-
  Prefix wrapped around a Bash command before the auto-mode permission
  classifier runs, stating it would run on another machine and quoting that
  machine's unverified ask reason.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_PERMISSION_CLASSIFIER_REMOTE_HOST_COMMAND_VAR_0
  - SYSTEM_PROMPT_PERMISSION_CLASSIFIER_REMOTE_HOST_COMMAND_VAR_1
  - SYSTEM_PROMPT_PERMISSION_CLASSIFIER_REMOTE_HOST_COMMAND_VAR_2
-->
# runs on ${SYSTEM_PROMPT_PERMISSION_CLASSIFIER_REMOTE_HOST_COMMAND_VAR_0.host.name} (another machine, not this one) in ${SYSTEM_PROMPT_PERMISSION_CLASSIFIER_REMOTE_HOST_COMMAND_VAR_0.host.working_dir}; that machine's Claude Code gave this reason for asking (its words, unverified): "${SYSTEM_PROMPT_PERMISSION_CLASSIFIER_REMOTE_HOST_COMMAND_VAR_1}"
