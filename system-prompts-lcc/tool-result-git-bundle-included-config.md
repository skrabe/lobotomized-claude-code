<!--
name: 'Tool Result: Git Bundle Included Config'
description: >-
  Upload refusal when git reads configuration for the checkout from a file a
  cloud session in the working tree could change or that cannot be examined.
ccVersion: 2.1.285
-->
Not uploading this working tree: git reads configuration for this checkout from a file that a cloud session in this working tree could change, or that cannot be examined from here, which this upload does not support. The file is one of these: the system-wide git configuration, ~/.gitconfig, ~/.config/git/config (or $XDG_CONFIG_HOME/git/config), what GIT_CONFIG_GLOBAL or GIT_CONFIG_SYSTEM names, the repository’s config or config.worktree, or a file that one of them includes. It is judged even if it does not exist yet, or if the include does not apply here. It lies inside this working tree or the repository’s git directory (other than that directory’s own config and config.worktree), is reached through a link that leads there, has a second name (a hard link), is on another host, or has a name that is not valid text. Keep that configuration elsewhere (or remove the include, the link or the second name), then retry.
