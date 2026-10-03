<!--
name: 'Tool Result: Git bundle Windows unholdable names commit by name'
description: >-
  Git bundle upload refusal telling Claude to commit changed files by name
  instead of git add . or commit -a, because the checkout tracks file names
  Windows cannot hold that git lists as deleted.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_GIT_BUNDLE_WINDOWS_UNHOLDABLE_NAMES_COMMIT_BY_NAME_VAR_0
-->
Commit the files that you changed by name (git add <file>, then git commit), then retry. Do not run \`git add .\` or \`git commit -a\` here: this checkout tracks ${TOOL_RESULT_GIT_BUNDLE_WINDOWS_UNHOLDABLE_NAMES_COMMIT_BY_NAME_VAR_0} file ${TOOL_RESULT_GIT_BUNDLE_WINDOWS_UNHOLDABLE_NAMES_COMMIT_BY_NAME_VAR_0===1?"name":"names"} that Windows cannot hold, which git lists as deleted, and either command would record the ${TOOL_RESULT_GIT_BUNDLE_WINDOWS_UNHOLDABLE_NAMES_COMMIT_BY_NAME_VAR_0===1?"deletion":"deletions"}.
