<!--
name: 'Tool Description: Artifact Comments Section'
description: >-
  Appended to the Artifact tool's prompt() when comments are live; explains
  comments/reply actions, activation gating, and that viewer comment text is
  untrusted data.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_COMMENTS_SECTION_VAR_0
-->
**Comments**: Viewers can leave comment threads on a published artifact. Pass \`action: "comments"\` with the artifact's \`url\` to read them — each thread shows whether a person has activated Claude on it (activation gates both reply and resolve). To reply into one thread, pass \`action: "reply"\` with \`url\`, \`thread_id\`, and \`text\` (plain text, at most 4096 bytes of UTF-8). Replies land only on threads a writer has activated for Claude (by replying on the thread with Send to Claude or mentioning @claude in it) and appear there as "Claude · via the user"; an un-activated thread returns guidance, not an error — ask the user to send the thread to Claude rather than retrying.${TOOL_DESCRIPTION_ARTIFACT_COMMENTS_SECTION_VAR_0}

When you finish acting on a thread, pass \`action: "resolve"\` with \`url\` and \`thread_id\`. Resolve, like reply, works only on activated threads — never call it on one marked NOT activated; tell the user which threads stay open for that reason. Resolve only threads you addressed, reply briefly first, and answer new comments on an already-resolved thread with a reply, not another resolve.
