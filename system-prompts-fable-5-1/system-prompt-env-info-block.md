<!--
name: Environment Info Block
description: >-
  Model-facing environment context block (T2m) 'Here is useful information about
  the environment you are running in:' with the <env>
  working-directory/git/platform/OS details, injected into the (sub)agent system
  prompt.
ccVersion: 2.1.191
variables:
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_0
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_1
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_2
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_3
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_4
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_5
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_6
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_7
  - SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_8
-->
Here is useful information about the environment you are running in:
<env>
Working directory: ${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_0()}
Is directory a git repo: ${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_1?"Yes":"No"}
${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_2}Platform: ${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_3.platform}
${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_4()}
OS Version: ${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_5}
${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_6?`${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_6}
`:""}</env>
${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_7}${SYSTEM_PROMPT_ENV_INFO_BLOCK_VAR_8}
