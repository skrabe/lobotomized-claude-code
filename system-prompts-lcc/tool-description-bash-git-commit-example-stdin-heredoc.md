<!--
name: 'Tool Description: Bash git committing — stdin heredoc commit example'
description: >-
  The git commit -F - heredoc command form the Bash tool description shows for
  passing a commit message when the stdin-heredoc form is required.
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_BASH_GIT_COMMIT_EXAMPLE_STDIN_HEREDOC_VAR_0
-->
git commit -F - <<'EOF'
Commit message here.${TOOL_DESCRIPTION_BASH_GIT_COMMIT_EXAMPLE_STDIN_HEREDOC_VAR_0.replace("   ","")}
EOF
