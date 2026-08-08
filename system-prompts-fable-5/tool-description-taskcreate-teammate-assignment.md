<!--
name: 'TaskCreate Description: Teammate Assignment Notes'
description: >-
  Conditional bullet block `t` built in Grp() and interpolated into the
  TaskCreate tool description when teams are enabled, telling the model to write
  descriptions another agent can act on and to assign owners via TaskUpdate.
ccVersion: 2.1.221
-->

- New tasks are created with status 'pending' and no owner - use TaskUpdate with the `owner` parameter to assign them
