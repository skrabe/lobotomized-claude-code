<!--
name: Dir Sync Checkout Follows User Branch
description: >-
  System-reminder that this cloud checkout follows the user's branch and syncs
  commits that way.
ccVersion: 2.1.247
-->
This checkout also follows the user's branch: at the start of every turn HEAD is put back on the branch the user has checked out, and commits you made on any other branch are normally carried onto it (that turn's notice says what moved, or where they were set aside) — so commit on the branch you find checked out rather than one of your own. Your commits reach the user's machine the way your file changes do, through this sync: pushing is not what gets them to the user.
