<!--
name: 'Tool Result: Remote Host Liveness Stream-Lost Clause'
description: >-
  unreachable detail interpolated into the session-channel host_offline
  tool_result when the liveness check failed because the event stream closed or
  the write was refused.
ccVersion: 2.1.261
-->
this session could not complete the liveness check for a reason on its own side (its event stream closed, the service refused the write that carried it, or that write had not completed in time); the machine was not reached and nothing was sent
