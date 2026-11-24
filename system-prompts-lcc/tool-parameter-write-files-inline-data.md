<!--
name: write_files data param
description: >-
  Input-schema param description for the DesignSync write_files inline
  file-contents (data) argument, now telling the model not to use it and to
  write a file under localDir and pass localPath instead.
ccVersion: 2.1.331
-->
Inline file contents (UTF-8 text, or base64 when encoding is "base64"). Do not use: write the content to a file at `path` under the localDir approved at finalize_plan, and pass localPath.
