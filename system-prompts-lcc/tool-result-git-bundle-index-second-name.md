<!--
name: 'Tool Result: Git Bundle Index Second Name'
description: >-
  Remedy clause when a cloud bundle upload refuses because the git index has a
  second name, telling the model to remove it and retry.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_SECOND_NAME_VAR_0
-->
 Git never gives it a second name, and through that name something else can change the file under git. Look at it (ls -l). Remove the other name if you can find it (\`find . -samefile\` with the file named above, run in this directory), or remove that file itself: ${TOOL_RESULT_GIT_BUNDLE_INDEX_SECOND_NAME_VAR_0}. Then retry.
