<!--
name: 'Tool result: connector upload asks for state-only retry'
description: >-
  Reason the connector's answer is refused: it asks for a retry with
  requestState and no input in a file-sending call
ccVersion: 2.1.325
-->
it asks for the call to be made again with its requestState and asks for no input (resultType "input_required" with no input request in it), which Claude Code does not do in a call that sends files; the files extension asks for uploads with resultType "upload_required"
