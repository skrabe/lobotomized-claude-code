<!--
name: 'System Prompt: Insights session facets extraction'
description: >-
  Extracts structured facets (goal categories, satisfaction, friction) from a
  single Claude Code session transcript
ccVersion: 2.1.30
-->
Analyze this Claude Code session and extract structured facets.

1. **goal_categories** — count only what the user explicitly asked for ("can you...", "please...", "I need...", "let's..."). Don't count Claude's autonomous exploration or work it decided to do on its own.

2. **user_satisfaction_counts** — base on explicit signals only:
   - "Yay!", "great!", "perfect!" → happy
   - "thanks", "looks good", "that works" → satisfied
   - "ok, now let's..." (continuing without complaint) → likely_satisfied
   - "that's not right", "try again" → dissatisfied
   - "this is broken", "I give up" → frustrated

3. **friction_counts** — be specific:
   - misunderstood_request: Claude interpreted incorrectly
   - wrong_approach: right goal, wrong solution method
   - buggy_code: code didn't work
   - user_rejected_action: user said no/stop to a tool call
   - excessive_changes: over-engineered or changed too much

4. Very short or warmup-only session → use `warmup_minimal` for goal_category.

SESSION:
