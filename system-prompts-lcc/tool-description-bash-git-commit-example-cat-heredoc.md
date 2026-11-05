<!--
name: 'Tool Description: Bash git committing — cat heredoc commit example'
description: >-
  The git commit -m "$(cat <<'EOF' …)" command form the Bash tool description
  shows for passing a multi-line commit message.
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_BASH_GIT_COMMIT_EXAMPLE_CAT_HEREDOC_VAR_0
-->
git commit -m "$(cat <<'EOF'
   Commit message here.${TOOL_DESCRIPTION_BASH_GIT_COMMIT_EXAMPLE_CAT_HEREDOC_VAR_0}
   EOF
   )"
