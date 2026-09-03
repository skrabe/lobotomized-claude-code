<!--
name: 'Data: Fork blocked — session started with restricting launch flags'
description: >-
  Tells the model why forking is refused (the copy would drop the parent's
  safety restrictions) and gives the two ways forward, so it does not retry
  /fork blindly.
ccVersion: 2.1.233
variables:
  - DATA_FORK_BLOCKED_RESTRICTED_LAUNCH_FLAGS_VAR_0
-->
Can't fork: this session was started with launch flags (safe or bare mode, ${DATA_FORK_BLOCKED_RESTRICTED_LAUNCH_FLAGS_VAR_0}) that the copy wouldn't inherit, so it would run with fewer restrictions than this session. Run the task here, or start a session without those flags and fork from there.
