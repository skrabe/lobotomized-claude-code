<!--
name: 'System Reminder: Ultrareview Post GitHub Token Rejected'
description: >-
  Tells the model GitHub rejected the stored account connection so the review
  was not posted, and to reconnect then post findings by hand.
ccVersion: 2.1.269
variables:
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_GITHUB_TOKEN_REJECTED_VAR_0
-->
GitHub no longer accepts the connection stored for your account, so nothing was posted. Reconnect GitHub at ${SYSTEM_REMINDER_ULTRAREVIEW_POST_GITHUB_TOKEN_REJECTED_VAR_0()} to post next time; the findings are above if you want to post them by hand now.
