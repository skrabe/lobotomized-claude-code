<!--
name: 'System Reminder: Background command stopped at deadline'
description: >-
  Tells the model a background command was stopped after reaching its background
  time limit: restart with run_in_background and a longer timeout only if the
  work still needs it and the longest timeout was not already used, and report
  that it was stopped
ccVersion: 2.1.285
-->
If the work in progress still needs it, start it again with `run_in_background` and a longer `timeout`. If it already had the longest `timeout` allowed, do not restart it. Either way, report that it was stopped.
