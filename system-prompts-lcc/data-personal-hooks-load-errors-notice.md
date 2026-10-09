<!--
name: 'Data: Personal hook load errors notice'
description: >-
  Notifies the model that some personal hooks did not load while other settings
  still apply.
ccVersion: 2.1.295
variables:
  - DATA_PERSONAL_HOOKS_LOAD_ERRORS_NOTICE_VAR_0
  - DATA_PERSONAL_HOOKS_LOAD_ERRORS_NOTICE_VAR_1
  - DATA_PERSONAL_HOOKS_LOAD_ERRORS_NOTICE_VAR_2
-->
Some hooks in ${DATA_PERSONAL_HOOKS_LOAD_ERRORS_NOTICE_VAR_0} have errors and won't run in this session. Your other hooks and settings still apply. To use them, fix these and start a new session:
${DATA_PERSONAL_HOOKS_LOAD_ERRORS_NOTICE_VAR_1(DATA_PERSONAL_HOOKS_LOAD_ERRORS_NOTICE_VAR_2)}
