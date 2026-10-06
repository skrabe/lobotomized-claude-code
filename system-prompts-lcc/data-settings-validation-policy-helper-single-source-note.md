<!--
name: Policy Helper Single-Source Note
description: >-
  Explains that policy-helper configuration keys are honored only from the
  single highest-priority managed settings source, even with
  managedSourcesBehavior "merge", and to configure the helper there instead.
ccVersion: 2.1.291
variables:
  - DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_0
  - DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_1
  - DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_2
-->
${DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_0.map((DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_1)=>`"${DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_1}"`).join(" and ")} in ${DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_2[Tt]} ignored: policy helper configuration is read from the highest managed settings source only (${DATA_SETTINGS_VALIDATION_POLICY_HELPER_SINGLE_SOURCE_NOTE_VAR_2[ge]} here), even with managedSourcesBehavior "merge". Configure the helper in that source instead.
