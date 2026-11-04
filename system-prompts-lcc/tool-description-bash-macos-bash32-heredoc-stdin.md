<!--
name: 'Bash tool: macOS bash 3.2 heredoc guidance'
description: >-
  Bash tool description note that macOS /bin/bash 3.2 cannot run heredocs inside
  $(...) and multi-line text must go on stdin or a single-quoted string.
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_BASH_MACOS_BASH32_HEREDOC_STDIN_VAR_0
  - TOOL_DESCRIPTION_BASH_MACOS_BASH32_HEREDOC_STDIN_VAR_1
-->
This tool runs macOS's /bin/bash (version 3.2), too old to run a heredoc inside \`$(...)\` reliably. Never write \`"$(cat <<'EOF' … EOF)"\`, even where other instructions show it. Pass multi-line text on stdin${TOOL_DESCRIPTION_BASH_MACOS_BASH32_HEREDOC_STDIN_VAR_0} and end the command at \`EOF\`: run what follows as a separate call. Where a command cannot read stdin, or a skill refuses ${TOOL_DESCRIPTION_BASH_MACOS_BASH32_HEREDOC_STDIN_VAR_1}, use one single-quoted string, writing each \`'\` as \`'\\''\`.
