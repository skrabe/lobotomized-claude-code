<!--
name: 'Tool Result: SendUserFile Declare Attached Outputs'
description: >-
  SendUserFile tool_result instruction to declare each shared-folder path on the
  reply via attached_outputs file refs.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_SENDUSERFILE_DECLARE_ATTACHED_OUTPUTS_VAR_0
  - TOOL_RESULT_SENDUSERFILE_DECLARE_ATTACHED_OUTPUTS_VAR_1
-->

To show ${TOOL_RESULT_SENDUSERFILE_DECLARE_ATTACHED_OUTPUTS_VAR_0(TOOL_RESULT_SENDUSERFILE_DECLARE_ATTACHED_OUTPUTS_VAR_1.length,"it","them")} on the thread, declare each path on your reply: attached_outputs: [{ "kind": "file", "ref": "<path above>" }].
