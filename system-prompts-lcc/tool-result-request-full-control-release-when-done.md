<!--
name: 'Tool Result: request_full_control release when done'
description: >-
  Suffix on full-screen approval advising release_full_control only after the
  last full-screen step.
ccVersion: 2.1.330
-->
 When no full-screen step is left in this task, call release_full_control to give the screen back. Do not call release_full_control between full-screen steps: that clears this approval, and the user would be asked again.
