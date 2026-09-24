<!--
name: SendFile network-mount path unsupported
description: >-
  SendFile attachment validation error returned to the model when an attachment
  path is under /net, /Network, /.vol, /.file, /.nofollow or /.resolve and could
  trigger a network mount; it tells the model to copy the file to a local path.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_SENDFILE_AUTOFS_HOSTS_UNSUPPORTED_VAR_0
-->
Attachment "${TOOL_RESULT_SENDFILE_AUTOFS_HOSTS_UNSUPPORTED_VAR_0}" is under /net, /Network, /.vol, /.file, /.nofollow or /.resolve, which could trigger a network mount, so it is not supported. Copy the file to an ordinary local path and pass that path instead.
