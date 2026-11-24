<!--
name: 'Slash command: PR Steward terms opens pull request first'
description: >-
  Explains that without a pull request Claude Code commits all changes, pushes,
  and opens one before watching
ccVersion: 2.1.331
-->
- Where your branch has no pull request yet, Claude Code first commits all your changes, on a new branch where needed, pushes the branch, and opens one. Claude writes the commit message from this session's conversation, and the pull request shows it. If the conversation doesn't cover your changes, Claude may write the pull request's title and description from the commit instead. You see them before the push. Your git hooks run. For a public repository, commit your work yourself first.
