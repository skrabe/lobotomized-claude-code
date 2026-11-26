<!--
name: 'Slash command: steward git submodule.recurse set'
description: >-
  submodule.recurse is on, so undoing a merge can fail or lose submodule work;
  shows how to find the setting
ccVersion: 2.1.332
-->
with submodule.recurse on in your git settings, undoing a merge can fail halfway or lose uncommitted work in a submodule (git config --show-origin --get-all submodule.recurse shows each file to change)
