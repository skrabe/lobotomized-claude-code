<!--
name: 'Tool Result: Git bundle refStorage set in ignored config'
description: >-
  Working-tree upload refusal reason when a git configuration file other than
  the repository's own config sets extensions.refStorage, listing the candidate
  files and telling to remove the key
ccVersion: 2.1.291
-->
a git configuration file other than this repository’s own config sets extensions.refStorage. git ignores that key there, but this upload does not start while git lists it with a location. The file is one of these: the system-wide git configuration, ~/.gitconfig, ~/.config/git/config (or $XDG_CONFIG_HOME/git/config), what GIT_CONFIG_GLOBAL or GIT_CONFIG_SYSTEM names, the repository’s config.worktree, or a file that one of them or the repository’s config includes. Remove the key from that file and retry
