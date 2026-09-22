<!--
name: 'Agent Prompt: Onboarding guide draft share link workflow'
description: >-
  Adds instructions for sharing the draft ONBOARDING.md before review, then
  updating the same ShareOnboardingGuide link after the user answers the review
  questions
ccVersion: 2.1.132
variables:
  - SHARE_ONBOARDING_GUIDE_TOOL_NAME
-->

**Sharing** — call the ${SHARE_ONBOARDING_GUIDE_TOOL_NAME} tool twice:

1. **Right after rendering the draft code block** (still in step 5, before the Review questions), call with \`mode='check'\` — this uploads the draft to an existing guide or creates a new one, returning a \`share_url\` and \`short_code\`. Instead of step 5's \`---\` / \`**Review**\` header, bridge from the link into the numbered questions (no horizontal rule):

   Here's a draft — a few quick questions to finish it up:

   <share URL>

   Then ask the three step-5 questions as normal. Save the \`short_code\` — you'll need it next.

2. **After the user answers and you've updated ONBOARDING.md**, call again with \`mode='update'\` and the \`short_code\` from step 1 to refresh the same link. Replace step 5's "drop it in your team docs" close with:

   Here's your onboarding guide: <updated URL>

   Send this to teammates and they'll get a guided walkthrough when they open it in Claude Code.

If the tool returns 'unavailable' at any point, skip that call and use the manual close from step 5.
