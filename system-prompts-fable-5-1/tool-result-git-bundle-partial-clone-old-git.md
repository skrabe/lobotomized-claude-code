<!--
name: 'Tool Result: Git Bundle Partial Clone Old Git'
description: >-
  Teleport git-bundle refusal when the checkout is a partial clone and installed
  git is too old to suppress promisor fetches.
ccVersion: 2.1.246
-->
Not uploading this working tree: the checkout is configured as a partial clone (a promisor remote), and the installed git is too old to be kept from fetching from that remote while the upload is prepared. Update git (2.45 or newer, or a current maintenance release of your version), or start from a full clone.
