<!--
name: 'System Reminder: Directory sync environment replaced, work restored'
description: >-
  Tells the agent its cloud container was recreated and its commits, staged
  state and working files were fully restored. Lists what was not restored:
  other branches, stashes, untracked files, tools and processes.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_ENVIRONMENT_REPLACED_WORK_RESTORED_VAR_0
-->
Directory sync: this session's cloud environment was REPLACED (the container was recreated) and your earlier work was RESTORED into this checkout: your commits, the staged state and the working files, including uncommitted ones, are as you left them at the end of your last turn (${SYSTEM_REMINDER_DIRECTORY_SYNC_ENVIRONMENT_REPLACED_WORK_RESTORED_VAR_0.branch===null?"at the commit you had checked out":"on the branch you had checked out"}; other local branches, stashes and repository settings you made in the earlier environment are not recreated); the user's newer changes, if any, are brought in as at any turn start. If a turn was under way when the environment was replaced, edits from that unfinished turn may not be here (this notice cannot tell) — check the files you last touched before building on them. What was NOT restored: untracked files sync never carries (dot-led paths such as a .env you wrote, dependency and build-output directories, credential-named or oversize files, nested repositories), anything outside the project directory, and the earlier environment's installed tools, caches and background processes — reinstall or restart what you need before relying on it, and do not assume a server or watcher you started earlier is still running.
