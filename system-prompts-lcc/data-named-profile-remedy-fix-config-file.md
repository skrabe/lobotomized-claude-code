<!--
name: 'Named Profile Remedy: Fix Config File'
description: >-
  Remedy telling the user to fix or delete the profile's config file, then unset
  or correct ANTHROPIC_PROFILE.
ccVersion: 2.1.331
variables:
  - DATA_NAMED_PROFILE_REMEDY_FIX_CONFIG_FILE_VAR_0
  - DATA_NAMED_PROFILE_REMEDY_FIX_CONFIG_FILE_VAR_1
  - DATA_NAMED_PROFILE_REMEDY_FIX_CONFIG_FILE_VAR_2
-->
Fix or delete ${DATA_NAMED_PROFILE_REMEDY_FIX_CONFIG_FILE_VAR_0===void 0?"`configs/<name>.json` in your Anthropic config directory (ANTHROPIC_CONFIG_DIR, if set)":DATA_NAMED_PROFILE_REMEDY_FIX_CONFIG_FILE_VAR_1(DATA_NAMED_PROFILE_REMEDY_FIX_CONFIG_FILE_VAR_2()??"","configs",`${DATA_NAMED_PROFILE_REMEDY_FIX_CONFIG_FILE_VAR_0}.json`)}, or 
