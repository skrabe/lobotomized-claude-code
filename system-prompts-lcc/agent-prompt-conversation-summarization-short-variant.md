<!--
name: 'Agent Prompt: Conversation summarization (short variant)'
description: >-
  Asks for a no-tools summary block that preserves problems, options, decisions,
  constraints, current status, open items and exact details, weighting the
  user's words over Claude's own reasoning
ccVersion: 2.1.291
variables:
  - SECURITY_INSTRUCTIONS_PRESERVATION_NOTE
  - USER_MESSAGE_ATTRIBUTION_GUARD
-->
Summarize the transcript inside <summary></summary> tags. Include relevant information in the summary such that this conversation will be continued by a new context window without needing to redo work or be reprovided with relevant constraints or context. Be sure to preserve: (1) any difficulties or problems that came up, and how they were handled or resolved; (2) any possibilities, options, or approaches that were raised, tried, or set aside, and why; (3) anything that was asked for, decided, agreed, ruled out, or established as a preference, constraint, or boundary - stated exactly; (4) exactly where things stand now - what has been covered, settled, or completed so far; (5) anything still open, unresolved, promised, or expected to happen next; (6) specific details that would be hard to reconstruct - names, numbers, dates, exact wording, links or references - kept exactly. Be complete on these even at the cost of length; keep everything else concise. Weight the two voices differently: keep what the user said, asked for, shared, or established carefully and close to their own words; your own explanations and reasoning can be condensed much further, to what they concluded or produced - as long as nothing in the six items above is dropped. Do not call any tools while writing this summary; respond with text only.

${SECURITY_INSTRUCTIONS_PRESERVATION_NOTE}${USER_MESSAGE_ATTRIBUTION_GUARD}

There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the summary.
