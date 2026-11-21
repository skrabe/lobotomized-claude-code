<!--
name: 'Tool result: app_type no answer before insert'
description: >-
  App stopped answering during read so nothing written; screenshot, retry once,
  or type regardless with risks.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_NO_ANSWER_BEFORE_INSERT_VAR_0
-->
the app stopped answering while this field was being read, so no text was written: a write sent now could land later, beside a retry. Take an app_screenshot, then retry the same call once; if this same refusal comes back, do not repeat it. To type regardless, ${TOOL_RESULT_APP_TYPE_NO_ANSWER_BEFORE_INSERT_VAR_0} (if the insert does not take, this can replace ALL of the field's content, which may not come back in the result; a write sent while the app does not answer can still land later)
