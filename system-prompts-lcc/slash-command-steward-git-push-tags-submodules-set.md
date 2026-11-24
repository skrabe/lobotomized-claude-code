<!--
name: 'Slash command: Steward git push tags or submodules set'
description: Refuses a git-only watch because pushes carry tags or submodules
ccVersion: 2.1.331
-->
your git settings send tags or submodules along with every push (push.followTags, push.recurseSubmodules, submodule.recurse), and this watch may push one branch alone (git config --show-origin --get-regexp "^(push|submodule)" lists them)
