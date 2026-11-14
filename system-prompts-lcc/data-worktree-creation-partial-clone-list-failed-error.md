<!--
name: Worktree creation missing objects not listed
description: Error that git could not list a partial clone's missing objects
ccVersion: 2.1.325
variables:
  - DATA_WORKTREE_CREATION_PARTIAL_CLONE_LIST_FAILED_ERROR_VAR_0
  - DATA_WORKTREE_CREATION_PARTIAL_CLONE_LIST_FAILED_ERROR_VAR_1
  - DATA_WORKTREE_CREATION_PARTIAL_CLONE_LIST_FAILED_ERROR_VAR_2
-->
This repository is a partial clone, and git could not list the objects needed for commit ${DATA_WORKTREE_CREATION_PARTIAL_CLONE_LIST_FAILED_ERROR_VAR_0} (${DATA_WORKTREE_CREATION_PARTIAL_CLONE_LIST_FAILED_ERROR_VAR_1}), so none were fetched before the checkout. ${DATA_WORKTREE_CREATION_PARTIAL_CLONE_LIST_FAILED_ERROR_VAR_2()?"Check that the repository is not damaged":'Check the repository with "git fsck"'} and try again.
