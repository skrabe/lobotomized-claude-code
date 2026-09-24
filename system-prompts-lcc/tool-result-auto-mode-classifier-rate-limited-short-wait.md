<!--
name: 'Tool Result: Auto mode classifier told to wait (short wait)'
description: >-
  Denial text for when the API tells auto mode's safety classifier to wait: do
  not retry this action or any other action that needs review until the wait
  ends, continue with work that needs no review, then retry.
ccVersion: 2.1.281
-->
Do not retry the action before then, and do not try any other action that needs auto mode's review: while the API still says to wait, each one is denied the same way, without being reviewed. Continue with work that needs no review, and try this action again once the wait is over. 
