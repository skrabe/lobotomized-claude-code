<!--
name: 'Tool Result: Cloud Session File Sync Tampered Git Object'
description: >-
  First-upload refusal line when an object in the project's .git does not match
  its name (git fsck names it); tells the model to remove it or re-clone before
  starting the cloud session.
ccVersion: 2.1.282
-->
An object in this project directory's .git holds something other than what its name vouches for, which git itself never writes (git fsck here names it). Remove whatever put it there, or clone the project again into a fresh directory, then start the cloud session there.
