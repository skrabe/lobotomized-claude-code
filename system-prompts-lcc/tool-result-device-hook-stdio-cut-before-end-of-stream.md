<!--
name: >-
  Tool Result: Device hook output incomplete because stdio was cut before
  end-of-stream
description: >-
  Block or deny reason returned to the cloud session when a hook run on the
  attached machine had its stdio cut before end-of-stream, so its output cannot
  be trusted and the call should be retried
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_DEVICE_HOOK_STDIO_CUT_BEFORE_END_OF_STREAM_VAR_0
-->
[${TOOL_RESULT_DEVICE_HOOK_STDIO_CUT_BEFORE_END_OF_STREAM_VAR_0}]: output incomplete — its stdio was cut before end-of-stream on this machine; retry
