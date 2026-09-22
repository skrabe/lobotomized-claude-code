<!--
name: 'Tool Result: Git Bundle Git File Pointer Unsupported'
description: >-
  Refuses the upload when .git is a pointer file the upload will not follow, and
  tells the model to start from the main checkout.
ccVersion: 2.1.280
-->
Not uploading this working tree: this checkout’s .git is a pointer file this upload does not follow (a submodule, a checkout with a separate git directory) or one it could not read, which it does not support yet. Start from an ordinary clone of the repository — its main checkout — instead.
