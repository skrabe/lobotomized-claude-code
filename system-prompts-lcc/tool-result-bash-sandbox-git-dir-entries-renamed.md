<!--
name: 'Bash tool result: sandbox renamed .git entries'
description: >-
  Note appended to a Bash result after the sandbox scrub renamed entries in a
  .git folder, explaining the effects and telling the model not to rename them
  back but to tell the user.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_BASH_SANDBOX_GIT_DIR_ENTRIES_RENAMED_VAR_0
-->
Claude Code renamed one or more entries in a .git folder so that git outside the sandbox does not follow them. Each now has a name like .<name>${TOOL_RESULT_BASH_SANDBOX_GIT_DIR_ENTRIES_RENAMED_VAR_0}<hex> in the same folder. Past 100 in one folder, links at index.stash.<pid> or fast_import_crash_<pid> are deleted, not renamed; that may not have happened here. If one was an ignore list, attributes file or hook, it no longer applies. If one was a branch or HEAD, that branch may be missing or at an older commit, and git may report no repository or use one in a folder above. Check before committing. Do not rename them back: tell the user.
