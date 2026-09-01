<!--
name: 'Skill: Code Review (--comment GitHub posting)'
description: >-
  Appended to the code-review prompt when --comment is passed; instructs posting
  each finding as an inline PR comment
ccVersion: 2.1.148
-->
## Posting to GitHub (--comment)

The \`--comment\` flag was passed. After producing the findings list, if the
review target is a GitHub PR, post each finding as an inline PR comment via
\`mcp__github_inline_comment__create_inline_comment\` (one call per finding;
include a suggestion block only when it fully fixes the issue). If that tool is
not available, fall back to \`gh api\` (repos/{owner}/{repo}/pulls/{pr}/comments)
or print the findings. If the target is not a PR, print the findings to the
terminal and note that \`--comment\` was ignored.
