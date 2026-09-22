<!--
name: 'Tool Description: Bash (sandbox — unenforced read denies)'
description: >-
  Relaxed sandbox sentence listing configured unread paths that still stand even
  though they are not enforced.
ccVersion: 2.1.268
variables:
  - TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_0
  - TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_1
  - TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_2
-->
Paths configured as not to be read, which stands even though it is not enforced here: ${TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_0(TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_1)}${TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_2.length>0?`, except ${TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_0(TOOL_DESCRIPTION_BASH_SANDBOX_UNENFORCED_READ_DENIES_VAR_2)}`:""}.
