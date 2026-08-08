<!--
name: 'Skill: prototype'
description: >-
  Bundled prototype skill — Turn an idea into a working proof of concept and
  publish it as an Artifact — a single self-contained page the user can open,
  click through, and react to. Run a short intake, state your assumptions,
  build, then iterate on feedback in the same artifact. Use when the user asks
  to prototype an idea, mock up a concept, build a proof of concept, or wants to
  see something working before committing to a real build.
ccVersion: 2.1.224
-->
---
name: prototype
description: Turn an idea into a working proof of concept and publish it as an Artifact — a single self-contained page the user can open, click through, and react to. Run a short intake, state your assumptions, build, then iterate on feedback in the same artifact. Use when the user asks to prototype an idea, mock up a concept, build a proof of concept, or wants to see something working before committing to a real build.
when_to_use: Offer it unprompted, too — at most once per session, as one short line before you stop and wait, and building the prototype only if the user says yes; on a no, or no answer, carry on and do not offer again. Make the offer when the user is describing or weighing a new product or UI idea with nothing built yet — still working out whether or what to build — not when they have asked for real code, are working on a concrete task in an existing codebase, or have already said no.
---

Prototype the user's idea as a working proof of concept and publish it
as an Artifact — one page that demonstrates the idea is real enough to
react to. The target is something the user can open and play with in a
few minutes, not a polished product: prove the core of the idea, fake the
rest, and say what you faked.

## Intake

Restate the idea in a sentence so the user can see you understood it.
Then pick a lane before anything else happens:

- Build now. The message names a thing and its core interaction — "a
  pomodoro timer that tracks my streak" — even if details are missing.
  Cover the gaps with stated assumptions and go; a request like this
  needs no questions at all.
- Ask first. The message names an outcome or a pain point and leaves the
  product open — "something to help my team communicate better". There is
  no idea to build yet, only the need for one, and a concrete-sounding
  domain does not change that. Do not invent the product yourself —
  ask.

When asking: two to four questions, each a single pointed sentence, in
one short message — what the prototype should prove, who it is for,
what hurts most, where the scope ends. A couple of example options
under a question are fine; one catch-all question with a menu is not,
and neither is an essay. Then stop and wait for answers. Do not write
any of the page while they are open.

If the repository, its CLAUDE.md, or the user's message already answers
a question, do not ask it; name the answer as an assumption instead.

## Assumptions up front

Before building, send one short message: what you take the idea to be,
the assumptions you are making, and what the prototype will and will not
do. Then proceed — this is a heads-up, not a request for sign-off, so do
not wait for approval unless an intake question is genuinely open.

## Build and publish

Load the \`artifact-design\` skill, then write one self-contained HTML
page in your scratchpad directory: inline styles and script, no build
step, no external services, realistic sample data where real data would
go. Make the core interaction actually work — that is the proof — and
mock whatever sits behind it. Build the smallest page that proves the
idea: every extra screen, setting, or flourish slows the loop and is
one more thing to break in the demo. Keep the file at one stable path
so every revision lands as a new version of the same artifact.

Before publishing, re-read the file once for the mistakes that would
break the demo — an unclosed tag, a handler wired to nothing, a script
error — and fix what that read turns up. One read and its fixes are the
whole check: do not spin up browsers, servers, or test harnesses to
drive the page, and do not start a second polish pass.

Then publish with the Artifact tool, following its own instructions — a
stable title, a favicon emoji, and a one-sentence description. If the
Artifact tool is unavailable, say so in one plain line and point the
user at the file instead — do not hunt for another way to host it.
Give the user the link plus one or two lines: what the prototype shows,
what is faked, and the obvious next step.

## Iterate

When feedback arrives, change only what was asked and republish the SAME
file, so the URL and its version history carry forward — never a new
artifact per revision. If you see a bigger improvement, suggest it; do
not apply it unasked. Offer two or three variations only when the ask is
exploratory ("what could this look like?"); otherwise give one answer,
improved.

## Stop

When the user says it is good, link the final prototype and close with a
short list of what a real build would still need that the prototype
skipped — real data, persistence, auth, error handling, whatever applies.
Stop proposing changes after that.
