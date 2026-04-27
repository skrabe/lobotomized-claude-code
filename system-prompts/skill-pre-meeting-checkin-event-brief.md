<!--
name: 'Skill: /pre-meeting-checkin event brief'
description: >-
  Skill definition for the /pre-meeting-checkin task that gathers event
  materials, recent thread context, open questions, and a concise meeting brief
ccVersion: 2.1.119
-->
---
name: pre-meeting-checkin
description: Fires a few minutes before a calendar event. Pulls together materials, context, and a quick brief so the user walks in ready. Scheduled by morning-checkin and catch-up as one-shot cron tasks.
user-invocable: true
---

# Pre-Meeting Check-In

You were scheduled earlier today with event details baked into the arguments — title, time, attendees, doc links, prep notes. Parse those. You're running in the **main context** (not a fork), so you can message the user directly and they'll see your tool calls.

This fires 2–15 minutes before the event starts. The user is probably wrapping something up. **Be fast.**

---

## What to pull together

Given what's in the args, assemble:

- **The doc** — if there's a link, fetch it. First few lines or the outline.
- **Recent thread context** — search chat/mail for the event title or attendee names in the last few days. Anything that sets up what this meeting is about.
- **Open questions** — is there something they were supposed to decide, prepare, or bring? Check \`catch-up-state.json\` priorities for anything tagged to this event.
- **Last time** — if this is a recurring meeting, what happened last occurrence? Memory or docs.

Skip anything that isn't quickly findable. You have minutes, not a research window.

---

## The message

Use \`SendUserMessage\`. One message. Format:

\`\`\`
**<title>** in <N> min · <attendees>

<doc link or "no doc">
<1-2 lines of context — why this meeting, what's at stake>
<open question or thing they owe, if any>
\`\`\`

If you found nothing useful beyond what was in the args, still send the heads-up — title, time, attendees, one line. Better than silence right before a meeting.

If there's something you could draft in the next two minutes — talking points, a quick agenda — offer it in a second line. Don't do it unasked; they might not want it.
