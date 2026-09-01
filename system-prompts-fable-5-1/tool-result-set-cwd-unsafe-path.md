<!--
name: Set Cwd Unsafe Path Rejection
description: >-
  The set_cwd tool result message returned to the model when the target path
  contains invisible/non-printing characters and cannot cross the trust
  boundary; model-facing.
ccVersion: 2.1.201
-->
The target path contains invisible or non-printing characters (control, formatting, zero-width, or non-standard space characters such as the narrow no-break space macOS puts in screenshot folder names), so it cannot safely cross the trust boundary. The path is deliberately not echoed back.
