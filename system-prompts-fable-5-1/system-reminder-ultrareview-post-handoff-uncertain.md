<!--
name: 'System Reminder: Ultrareview Post Handoff Uncertain'
description: >-
  Warns the model that handing findings to claude.ai raised an exception and
  that the pull request should be checked before manual posting.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_HANDOFF_UNCERTAIN_VAR_0
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_HANDOFF_UNCERTAIN_VAR_1
-->
The findings couldn't be handed to claude.ai for posting (${SYSTEM_REMINDER_ULTRAREVIEW_POST_HANDOFF_UNCERTAIN_VAR_0(SYSTEM_REMINDER_ULTRAREVIEW_POST_HANDOFF_UNCERTAIN_VAR_1)}). Check the pull request before posting by hand — if the request got through, the comment may still appear.
