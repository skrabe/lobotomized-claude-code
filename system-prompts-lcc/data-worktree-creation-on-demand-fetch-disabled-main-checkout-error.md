<!--
name: 'Data: Worktree creation on-demand fetch disabled (main checkout fetch) error'
description: >-
  Worktree creation error suffix when git on-demand fetching was off: fetch the
  missing commit objects in the main checkout if a partial clone, otherwise
  check for damage
ccVersion: 2.1.325
variables:
  - DATA_WORKTREE_CREATION_ON_DEMAND_FETCH_DISABLED_MAIN_CHECKOUT_ERROR_VAR_0
-->

This checkout ran with git's on-demand fetching switched off, and git needed an object this repository does not have. If the repository is a partial clone, fetch the missing objects for commit ${DATA_WORKTREE_CREATION_ON_DEMAND_FETCH_DISABLED_MAIN_CHECKOUT_ERROR_VAR_0} in its main checkout yourself and try again. If it is not a partial clone, it may be damaged: check it, then try again.
