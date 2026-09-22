<!--
name: 'Tool Result: Git Bundle Previous Way Gitlinks'
description: >-
  w6 refusal when the previous upload path would enter nested gitlinks under
  configuration a session of this checkout can write.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_2
-->
It is not uploaded the previous way either: this checkout's index registers ${TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_0.length} nested ${TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_1(TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_0.length,"repository","repositories")} (a submodule or gitlink: ${TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_2(TOOL_RESULT_GIT_BUNDLE_PREVIOUS_WAY_GITLINKS_VAR_0,3)}), which that way would enter, running git under the nested repository’s own configuration — one a session of this checkout can write. If the entry is not meant, remove it from the index with \`git update-index --force-remove -- <path>\` (not \`git rm\`, which first runs git inside the nested repository); otherwise update git (2.31 or newer) if it is older, or start from an ordinary clone.
