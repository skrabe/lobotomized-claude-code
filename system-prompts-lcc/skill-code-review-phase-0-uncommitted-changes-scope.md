<!--
name: 'Skill: Code Review phase 0 uncommitted changes scope'
description: Adds working-tree changes and named targets to the review scope
ccVersion: 2.1.330
-->
If there are
uncommitted changes, or the range diff is empty, also run \`git diff HEAD\` and
include the working-tree changes in scope — the review often runs before the
commit. If a PR number, branch name, or file path was passed as an argument,
review that target instead. Treat this diff as the review scope.
