<!--
name: 'Slash Command: Steward - comment body heredoc'
description: >-
  Heredoc form of the gh comment body, with the hidden marker and the Claude
  Code author line, given in /steward's command set.
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_STEWARD_COMMENT_BODY_HEREDOC_VAR_0
  - SLASH_COMMAND_STEWARD_COMMENT_BODY_HEREDOC_VAR_1
-->
"$(cat <<'${SLASH_COMMAND_STEWARD_COMMENT_BODY_HEREDOC_VAR_0}'
${SLASH_COMMAND_STEWARD_COMMENT_BODY_HEREDOC_VAR_1} -->
Claude Code here, for the author: ...
${SLASH_COMMAND_STEWARD_COMMENT_BODY_HEREDOC_VAR_0}
)"
