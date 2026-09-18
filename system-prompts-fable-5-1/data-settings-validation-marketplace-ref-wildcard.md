<!--
name: 'Data: Settings Validation Marketplace Ref Wildcard'
description: >-
  Reason fragment for a github/git marketplace policy entry whose ref contains
  "*", which git does not allow in ref names, so the entry cannot be enforced;
  interpolated into the managed-settings validation issue.
ccVersion: 2.1.277
variables:
  - DATA_SETTINGS_VALIDATION_MARKETPLACE_REF_WILDCARD_VAR_0
-->
${DATA_SETTINGS_VALIDATION_MARKETPLACE_REF_WILDCARD_VAR_0.source}: ref contains "*", which git does not allow in ref names; the entry cannot be enforced
