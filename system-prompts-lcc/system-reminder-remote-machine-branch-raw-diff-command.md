<!--
name: 'System Reminder: Remote machine branch transfer — raw diff command'
description: >-
  The exact git command (git -c core.quotePath=true -c diff.relative=false diff
  --raw --ignore-submodules=none HEAD <sha>) the model runs on the remote
  machine to show the user what a transferred branch changes; also embedded in
  the sensitive-path diff command.
ccVersion: 2.1.277
-->
git -c core.quotePath=true -c diff.relative=false diff --raw --ignore-submodules=none HEAD <sha>
