<!--
name: 'Skill: /morning-checkin daily brief'
description: >-
  Skill definition for the /morning-checkin scheduled task that prepares a daily
  calendar and inbox digest, schedules pre-meeting check-ins, and records the
  day’s top priority
ccVersion: 2.1.119
-->
---
name: morning-checkin
description: Once-a-day scan in the two hours before work starts — calendar prep, pre-meeting scheduling, overnight mail/chat/docs digest, and a brief that gets the user ready for the day.
user-invocable: true
context: fork
---

# Morning Check-In

This fires **once a day** randomly in the two hours before their work day starts, or somewhere between 7am and 9am local if we don't know when their workday starts. The default 7am–9am window was baked into \`.claude/scheduled_tasks.json\` at install time — once the user fills in Catch-up hours in \`CLAUDE.md\`, rewrite that cron entry to land two hours before their actual start time (cron is local time, so just use the local hour directly). You're running in a fork — tool calls like \`CronCreate\` execute and persist to disk, but the **only thing the main agent sees is your final text**. Build the digest there; the main agent decides whether to relay.

Read \`CLAUDE.md\` for who they are (name, timezone, handles) and \`.claude/catch-up-state.json\` for what you were already tracking.

---

## Is it still morning?

The cron pins your intended fire time, but the scheduler catches up on delayed startup — laptop closed overnight, opened at 3pm → you fire at 3pm. Don't brief then; catch-up has been running for hours and has the day covered.

Check the local time against the start of their Catch-up hours from \`CLAUDE.md\` (default 9am if blank). If you're **more than two hours past work start**, end with a single line:

\`\`\`
(not morning)
\`\`\`

Main agent won't relay this. Don't scan anything, don't write state.

A fire at 9:30am for a 9am work start is fine (within the window — brief is still useful). A fire at 11:30am is not (catch-up has it). If the user runs you manually at an odd hour, the main agent will see \`(not morning)\` come back and can override by telling the user what's up — that's its call to make.

---

## Phase 1 — Calendar

**Only if a calendar tool is connected.** If not, skip to Phase 2.

Pull today's events (user's local timezone, work-start through end of day). For each event, note:

- **Title, time, attendees**
- **Your response status** — if you haven't RSVP'd, flag it.
- **Prep signals** — description mentions a doc, agenda, presentation, pre-read? Attendee list suggests a review where something is expected of you? Recurring meeting where you usually bring something?
- **Materials on hand** — search docs/drive for anything matching the event title or linked from the invite. Do we have a draft, or nothing?

### Schedule pre-meeting check-ins

For each event with a concrete start time, schedule a one-shot reminder that will pull materials together right before it starts. Pick a random offset between **2 and 15 minutes** before the event (vary it per event — don't stack everything at the same offset). Subtract the offset from the event's local start time, then:

\`\`\`
CronCreate(
  cron: "<minute> <hour> <day-of-month> <month> *",   # local time, pinned
  prompt: "/pre-meeting-checkin <title> · <local time> · <attendees> · <any doc links or prep notes>",
  recurring: false
)
\`\`\`

Use \`recurring: false\` — these fire once and self-delete. \`CronList\` first and skip any event that already has a matching pre-meeting prompt scheduled (don't double-book if the user re-runs you manually, or catch-up got to an event first).

---

## Phase 2 — Overnight inbox

Scan what landed since end of the previous work day. Only tools that are actually connected — adapt.

- **Mail** — unread from people or domains that matter (boss, reports, key collaborators — \`CLAUDE.md\` and \`catch-up-state.json\` priorities tell you who). Not a full inbox sweep — top 3-5 that actually need attention today.
- **Chat** — mentions, DMs, threads with activity where you're a participant. Same filter: what needs a response today vs. what's ambient.
- **Docs** — new docs shared with you, or comments/edits on docs you own, since yesterday.

For each: one line. Sender/author, subject, why it matters today.

---

## Phase 3 — Shape of the day

From calendar density + inbox signals + \`catch-up-state.json\` priorities, infer the **one thing** that most needs to go well today. A meeting that needs prep, a deadline, a thread that's been waiting on you.

If there's a natural check-in point for it — an hour before a deadline, after a block of free time ends — schedule it:

\`\`\`
CronCreate(
  cron: "<minute> <hour> <day-of-month> <month> *",   # local time, pinned
  prompt: "Check-in: <thing>. Where are we? What's blocking?",
  recurring: false
)
\`\`\`

Don't over-schedule. Zero or one of these. Catch-up runs every two hours and will notice if something changes.

Write today's top priority into \`catch-up-state.json\` under \`priorities\` so catch-up picks it up.

---

## Phase 4 — The brief

Your final text is the digest. This is what the main agent sees and relays. **Brief. Scannable. Hierarchy.**

\`\`\`
**<Day, Date>** · <N> meetings · <M> things need you

**Calendar**
  <time>  <title>  <· unresponded | · prep needed | (blank if fine)>
  <time>  <title>

**Needs you**
  · <sender/thread> — <one line>
  · <sender/thread> — <one line>

**Top priority:** <the one thing>

<I can: draft the agenda for X / prep slides for Y / reply to Z. Say which.>
\`\`\`

Drop any section that's empty. If the calendar is clear and nothing needs them, the whole brief is three lines. The goal is they glance at this and know what the day looks like — not that they read a report.

On a weekend with nothing scheduled and nothing in the inbox, it's fine for the whole thing to be one line: \`**<Day>** · nothing on.\` Don't invent work to report.

One-shot pre-meeting check-ins are already scheduled — don't list them in the brief, they'll fire on their own.
