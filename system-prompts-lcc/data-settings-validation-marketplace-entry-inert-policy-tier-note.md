<!--
name: 'Data: Settings Validation Marketplace Entry Inert Outside Policy Tiers'
description: >-
  Settings-validation line for a strict/blocked-marketplaces entry that can
  never match: explains that policy tiers keep or strip it and that in
  user/project/local files the key is inert, and asks for the entry to be fixed
  or removed
ccVersion: 2.1.277
variables:
  - DATA_SETTINGS_VALIDATION_MARKETPLACE_ENTRY_INERT_POLICY_TIER_NOTE_VAR_0
  - DATA_SETTINGS_VALIDATION_MARKETPLACE_ENTRY_INERT_POLICY_TIER_NOTE_VAR_1
  - DATA_SETTINGS_VALIDATION_MARKETPLACE_ENTRY_INERT_POLICY_TIER_NOTE_VAR_2
-->
${DATA_SETTINGS_VALIDATION_MARKETPLACE_ENTRY_INERT_POLICY_TIER_NOTE_VAR_0}[${DATA_SETTINGS_VALIDATION_MARKETPLACE_ENTRY_INERT_POLICY_TIER_NOTE_VAR_1}]: ${DATA_SETTINGS_VALIDATION_MARKETPLACE_ENTRY_INERT_POLICY_TIER_NOTE_VAR_2} — on policy tiers (managed settings) ${DATA_SETTINGS_VALIDATION_MARKETPLACE_ENTRY_INERT_POLICY_TIER_NOTE_VAR_0==="blockedMarketplaces"?"clients keep it with a warning, but it can never match, so it blocks nothing":"clients silently strip it at load"}; in user/project/local files the key is inert; fix or remove the entry
