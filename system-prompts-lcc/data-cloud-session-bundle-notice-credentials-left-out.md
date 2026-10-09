<!--
name: 'Cloud Session Bundle Notice: Credential Files Left Out'
description: >-
  Notice that uncommitted files named like credentials stayed on this machine
  when the working tree was bundled for a cloud session; part of the
  /ultrareview branch launch text the model reads.
ccVersion: 2.1.295
variables:
  - DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0
  - DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_1
  - DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_2
  - DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_3
-->
Left on this machine: ${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0.length} uncommitted ${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_1(DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0.length,"file")} named like credentials or keys, ${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_2?"covered by a Read rule or a sandbox read-deny setting of yours, linked from your Claude Code configuration, ":""}hard-linked to another file, kept by a git filter such as LFS, or still being written by another program while ${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_1(DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0.length,"it was","they were")} read (${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_3(DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0)}), ${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_1(DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0.length,"was","were")} not uploaded — the cloud session starts with the version git already holds for ${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_1(DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0.length,"it","them")} (committed or staged), or without ${DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_1(DATA_CLOUD_SESSION_BUNDLE_NOTICE_CREDENTIALS_LEFT_OUT_VAR_0.length,"it","them")}.
