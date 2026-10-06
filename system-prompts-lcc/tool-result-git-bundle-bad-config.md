<!--
name: 'Tool Result: Git bundle bad config'
description: >-
  Upload refusal when git cannot parse one of its configuration files, advising
  git rev-parse --git-dir to locate the fault
ccVersion: 2.1.291
-->
Git cannot parse one of its configuration files (“bad config”), so nothing was uploaded. Run `git rev-parse --git-dir` here (it changes nothing): its error names the file and the line, or the setting at fault. Fix that, then retry.
