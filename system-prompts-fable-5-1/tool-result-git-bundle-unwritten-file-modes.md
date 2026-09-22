<!--
name: Unwritten File Modes
description: >-
  Cloud-session creation failure telling the model the index contains file modes
  git never writes.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_2
-->
It is not uploaded the previous way either: this checkout's index lists ${TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_0.length} ${TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_1(TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_0.length,"entry","entries")} under a file mode git itself never writes (${TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_2(TOOL_RESULT_GIT_BUNDLE_UNWRITTEN_FILE_MODES_VAR_0,3)}), so something other than git wrote the index and what the previous way would carry cannot be checked. Remove each such entry with \`git update-index --force-remove -- <path>\` (the file itself stays on disk), then \`git add -- <path>\` if it should be tracked; or start from an ordinary clone.
