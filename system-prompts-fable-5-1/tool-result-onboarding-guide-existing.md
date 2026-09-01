<!--
name: Onboarding guide already exists result
description: >-
  ShareOnboardingGuide tool_result data.message telling the model an org guide
  already exists and how to proceed.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_ONBOARDING_GUIDE_EXISTING_VAR_0
-->
A guide already exists for this org at ${TOOL_RESULT_ONBOARDING_GUIDE_EXISTING_VAR_0.share_url} (short_code: ${TOOL_RESULT_ONBOARDING_GUIDE_EXISTING_VAR_0.short_code}). If this link is what the user needed, share it. If they want to create or update a guide, tell them to run /team-onboarding themselves (it scans local session data and cannot be invoked by the model).
