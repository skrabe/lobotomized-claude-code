<!--
name: 'Slash Command: /plugin tag — tags need explicit semver note'
description: >-
  Appended to the /plugin tag no-version error: tags only serve dependency
  version constraints and older-version lookup, which need an explicit semver;
  the git-SHA fallback needs no tag
ccVersion: 2.1.325
-->
 Tags are only used for dependency version constraints and for finding an older version that fits this Claude Code, which require an explicit semver — the git-SHA fallback does not need a tag.
