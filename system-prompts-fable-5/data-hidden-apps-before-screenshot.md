<!--
name: 'Data: Hidden apps before screenshot'
description: >-
  Content block telling the model which apps were hidden (not in the allowlist)
  before a screenshot.
ccVersion: 2.1.246
variables:
  - DATA_HIDDEN_APPS_BEFORE_SCREENSHOT_VAR_0
  - DATA_HIDDEN_APPS_BEFORE_SCREENSHOT_VAR_1
-->
${DATA_HIDDEN_APPS_BEFORE_SCREENSHOT_VAR_0} ${DATA_HIDDEN_APPS_BEFORE_SCREENSHOT_VAR_1?"was":"were"} open and got hidden before this screenshot (not in the session allowlist). If a previous action was meant to open ${DATA_HIDDEN_APPS_BEFORE_SCREENSHOT_VAR_1?"it":"one of them"}, that's why you don't 
