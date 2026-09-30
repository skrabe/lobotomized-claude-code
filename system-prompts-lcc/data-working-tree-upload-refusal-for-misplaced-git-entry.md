<!--
name: 'Data: Working tree upload refusal for misplaced .git entry'
description: >-
  Error refusing a working-tree upload because the checkout's .git is a pointer
  file, symbolic link, hard-linked pointer file, or otherwise unfollowable
  entry, telling the user to start from the repository's ordinary main checkout
  instead
ccVersion: 2.1.285
variables:
  - GIT_DIR_MISPLACEMENT_RESULT
-->
Not uploading this working tree: ${GIT_DIR_MISPLACEMENT_RESULT.pointerFollowed?"this checkout’s .git is a pointer file (a submodule, a checkout with a separate git directory), which this upload does not support yet. Before running any git command here, look at the directory that it leads to (the .git file names it), unless you know it. Start":GIT_DIR_MISPLACEMENT_RESULT.dotGitEntry==="link"?"this checkout’s .git is a symbolic link, which this upload does not follow. Start":GIT_DIR_MISPLACEMENT_RESULT.dotGitEntry==="second_name"?"this checkout’s .git pointer file has a second name (a hard link), so what it names cannot be trusted. Remove the other name and retry, or start":"this checkout’s .git is something this upload could not follow (it could not be read, is not the one gitdir line git writes, or names another host). Start"} from an ordinary clone of the repository — its main checkout — instead.
