<!--
name: ShareOnboardingGuide tool description
description: >-
  Tool description for the ShareOnboardingGuide tool, injected into the model's
  tool set.
ccVersion: 2.1.206
-->
Upload the ONBOARDING.md in the current directory and return a share link teammates can open in Claude Code. Call this after the user has confirmed the final content.

When called with the default mode='check': if a local ONBOARDING.md is present, uploads it to the most-recently-updated org guide (or creates one if none exist) and returns a fresh link. If no local file is present, returns the existing link without uploading (status: has_existing).
