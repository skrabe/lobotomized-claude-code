<!--
name: 'Tool Result: Git Bundle Borrowed Objects'
description: >-
  Refuses the upload when the checkout borrows objects via
  objects/info/alternates, which could carry another repository's history.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_GIT_BUNDLE_BORROWED_OBJECTS_VAR_0
-->
Not uploading this working tree: this checkout borrows objects from another repository (an objects/info/alternates or http-alternates file — a clone made with --shared or --reference, or a file something else put there), so an upload could carry that repository’s history too, which this upload does not support. Start from an ordinary clone, or repack the checkout (git repack -a -d) and remove the alternates file if nothing relies on it.${TOOL_RESULT_GIT_BUNDLE_BORROWED_OBJECTS_VAR_0.sharedDirectoryElsewhere?" (This checkout is a linked working tree: that file is in its repository’s git directory, which this checkout’s .git file points into.)":""}
