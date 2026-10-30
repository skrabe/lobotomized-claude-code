<!--
name: 'Tool Description: Bash run_in_background Detached'
description: >-
  Bash tool description fragment explaining run_in_background runs detached and
  re-invokes on exit.
ccVersion: 2.1.314
variables:
  - TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_0
  - TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_1
  - TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_2
  - TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_3
  - TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_4
  - TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_5
-->
- \`run_in_background\` runs the command detached${TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_0?", and you are notified if it exits while you are still working":": it keeps running across turns and re-invokes you when it exits"}.${TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_1()?` With it, \`timeout\` is how long the command may run in the background (default ${TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_2()}, max ${TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_3()}); at that limit it is stopped${TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_0?"":" and you are re-invoked"}.`:""}${TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_4()}${TOOL_DESCRIPTION_BASH_RUN_IN_BACKGROUND_DETACHED_VAR_5()}
