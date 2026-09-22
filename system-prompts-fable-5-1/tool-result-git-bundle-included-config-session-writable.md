<!--
name: 'Tool Result: Git Bundle Included Config Session Writable'
description: >-
  r6.included_config clause refusing the upload when git config includes a file
  a session can write.
ccVersion: 2.1.280
-->
its git configuration includes a file a session can write, so that capture would run under whatever is put there; keep that configuration outside the working tree (or remove the include)
