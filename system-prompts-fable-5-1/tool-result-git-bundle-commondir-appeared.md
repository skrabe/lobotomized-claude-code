<!--
name: 'Tool Result: Git Bundle Commondir Appeared'
description: >-
  Refuses the upload when a commondir file appears in the git directory while
  the upload is prepared.
ccVersion: 2.1.280
-->
Not uploading this working tree: a commondir file appeared in its git directory while the upload was prepared — git writes one only in a linked working tree’s entry — so what was packed cannot be vouched for. Inspect the git directory, then retry.
