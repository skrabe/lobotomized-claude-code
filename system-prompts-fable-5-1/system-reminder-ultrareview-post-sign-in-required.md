<!--
name: 'System Reminder: Ultrareview Post Sign-In Required'
description: >-
  Tells the model posting needs a working Claude sign-in so nothing went to the
  pull request, and to run /login then post findings by hand.
ccVersion: 2.1.269
variables:
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_SIGN_IN_REQUIRED_VAR_0
-->
Posting needs a working Claude sign-in here${SYSTEM_REMINDER_ULTRAREVIEW_POST_SIGN_IN_REQUIRED_VAR_0?` (${SYSTEM_REMINDER_ULTRAREVIEW_POST_SIGN_IN_REQUIRED_VAR_0})`:""}, so nothing went to the pull request. Run /login to fix that for next time; the findings are above if you want to post them by hand now.
