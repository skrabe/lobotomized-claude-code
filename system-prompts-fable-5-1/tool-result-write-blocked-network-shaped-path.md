<!--
name: 'Tool Result: Write Blocked — Network-Shaped Path'
description: >-
  Error message returned from Edit/Write validateInput when the target path is a
  UNC share or /net automount spelling while the session checkout is local;
  delivered to the model as the failed tool result.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_WRITE_BLOCKED_NETWORK_SHAPED_PATH_VAR_0
-->
This write was blocked because the path is network-shaped (a UNC share or /net automount spelling) while this session's checkout is local. Isolating cannot unblock it. ${TOOL_RESULT_WRITE_BLOCKED_NETWORK_SHAPED_PATH_VAR_0===void 0?"If the file is genuinely local, retry the edit addressing it by its local, plainly-spelled path.":`If the file is genuinely inside the worktree ${TOOL_RESULT_WRITE_BLOCKED_NETWORK_SHAPED_PATH_VAR_0}, address it by its local, plainly-spelled path instead.`}
