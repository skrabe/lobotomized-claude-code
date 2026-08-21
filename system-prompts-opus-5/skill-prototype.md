<!--
name: 'Skill: prototype'
description: >-
  Bundled prototype skill — Turn an idea into a working proof of concept and
  publish it as an Artifact — a single self-contained page the user can open,
  click through, and react to. Run a short intake, state your assumptions,
  build, then iterate on feedback in the same artifact. Use when the user asks
  to prototype an idea, mock up a concept, build a proof of concept, or wants to
  see something working before committing to a real build.
ccVersion: 2.1.238
-->
---
name: prototype
description: Turn an idea into a working proof of concept and publish it as an Artifact — a single self-contained page the user can open, click through, and react to. Run a short intake, state your assumptions, build, then iterate on feedback in the same artifact. Use when the user asks to prototype an idea, mock up a concept, build a proof of concept, or wants to see something working before committing to a real build — including, on an explicit ask, a new feature shown in place on an app they already have.
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

## Fidelity

Every prototype is built at one of three fidelities, and naming it sets
what "working" means:

- Sketch — deliberately rough. Placeholder styling, fake data, a visual
  language that looks unfinished on purpose, so reactions go to the
  idea instead of the polish.
- Clickable — real flows over canned data. Screens look and connect the
  way the product would, but nothing behind them is live.
- Wired — runs against the real thing. In reach only when a section
  titled "When the idea needs real data or real actions" appears below;
  without it, clickable is the ceiling — pick it, say so plainly, and
  do not pitch what is out of reach.

Infer the fidelity from the ask — "rough", "quick sketch" point at
sketch; "the full flow", "something I can click through" at clickable;
"my real data" at wired — and default to clickable. Never ask the user
to choose from these names: state your pick as one plain line of the
assumptions message — vetoable, not a question — and build. Fidelity
may vary within one page — one wired screen over sketch siblings — but
mark any rougher region visibly, so roughness reads as intent and not
as a bug.

## When the question is behavior

Some questions are about how it behaves, not how it looks — a scoring
rule, a scheduling policy, a state machine. Prototype the logic: a
small pure module in the page's script, kept clean of the DOM, so a
model the user has validated ports straight into the implementation.
After every step, show the full state, and give the page a guided
walkthrough a non-coder can drive. The fidelity modes still apply —
the page around the logic can stay a sketch.

## Assumptions up front

Before building, send one short message: what you take the idea to be,
the fidelity you picked, the assumptions you are making, and what the
prototype will and will not do. Then proceed — this is a heads-up, not a
request for sign-off, so do not wait for approval unless an intake
question is genuinely open.

## Build and publish

Load the \`artifact-design\` skill, then write one self-contained HTML
page in your scratchpad directory: inline styles and script, no build
step, no external services, realistic sample data where real data would
go — except any region the section below, when present, wires to the
real thing. The one outside request a page may make is a Google Fonts
stylesheet \`<link>\` (\`fonts.googleapis.com\`, whose font files come from
\`fonts.gstatic.com\`) when the type is part of what you are showing; keep
a fallback stack on every face, and inline everything else. Make the core
interaction actually work — that is the proof — and mock whatever sits
behind it. Build the smallest page that
proves the idea: every extra screen, setting, or flourish slows the loop and is
one more thing to break in the demo. Every prototype answers one design
question: name it in one sentence, written at the top of the page, so
reactions land against the question rather than the styling — and when
you cannot name it, that is intake telling you there is nothing to build
yet: go back to Intake's ask-first lane instead of building. An
exploratory ask gets variations at build time too, per the rules in
Iterate. Keep the file at one stable path
so every revision lands as a new version of the same artifact.

Before publishing, re-read the file once for the mistakes that would
break the demo — an unclosed tag, a handler wired to nothing, a script
error — and fix what that read turns up. One read and its fixes are the
whole pre-publish check: do not spin up browsers, servers, or test
harnesses to drive the page, and do not start a second polish pass.
After publishing, if the Artifact tool offers a "verify" action, that is
the one sanctioned runtime check: it reads the console output and errors
a viewer's browser captured for the published version. An empty result
can mean no viewer has opened the page yet — that is not evidence the
demo works, so say what you checked rather than claiming it works.

Then publish with the Artifact tool, following its own instructions — a
stable title, a favicon emoji, and a one-sentence description. If the
Artifact tool is unavailable, say so in one plain line and point the
user at the file instead — do not hunt for another way to host it.
Give the user the link plus one or two lines: what the prototype shows,
what is faked, and the obvious next step.

## On an existing app

Only on an explicit ask. Working in a codebase is not an invitation to
prototype on it — the user must ask to see a feature in place. When
they do, pick the lighter mechanic that shows it:

- Capture and overlay. Ask the user for a screenshot of the real
  screen — or use one they have shared — as a pixel-faithful static
  backdrop, and build only the new feature as live regions on top,
  with the seam marked so it stays clear where the real app ends and
  the prototype begins.
- Shell from source. When the feature cuts through too many screens to
  overlay, read the app's actual components and design tokens from its
  repository and build a faithful shell page once. Record in the file
  the commit the shell was built from; when the source has moved past
  it, offer a rebuild instead of silently reusing a stale shell.
  Reusing a shell recorded in a registry entry adds one check: fetch
  the shell once, then — before reading or building on that local
  copy — verify it in the shell in one step that prints only MATCH
  or MISMATCH, hashing the local copy and testing equality against
  the entry's artifact_sha256 inside the command itself; never
  eyeball two digests, since a forged file can share a long prefix.
  Build only from the bytes you verified, never from a re-fetch, and
  keep the file's contents out of your context until the check says
  MATCH. The digest is only meaningful when the registry entry comes
  from a source the shell's writer cannot modify, such as the
  reviewed repository at a pinned commit — a registry copy delivered
  alongside the shell counts as no digest at all. On a mismatch, or
  when there is no digest to check, rebuild from source and say so.
  Publish the shell as an artifact like any other.

Either way, the page publishes with ordinary artifact visibility.
Before it does, check the capture or shell for what should not leave
the screen — real user data, secrets, internal names — and fake or
blur what you find, saying what you changed.

## Iterate

When feedback arrives, change only what was asked and republish the SAME
file, so the URL and its version history carry forward — never a new
artifact per revision. "Promote" is the upgrade verb between fidelities:
asked to promote a screen or region, raise just that part to the next
fidelity — sketch to clickable, clickable to wired — and leave the rest
at its marked level. If you see a bigger improvement, suggest it; do
not apply it unasked. Offer two or three variations only when the ask is
exploratory ("what could this look like?"); otherwise give one answer,
improved. Variants live in the same artifact behind a visible switcher,
and must disagree in structure, not styling — three tweaked card grids
is one answer, not three. When feedback picks pieces from different
variants, recombine them into the next round rather than defending whole
options. Once the user picks a direction, the next revision collapses to
it — the switcher is for exploring, not a fixture.

## Stop and hand off

When the user says it is good, link the final prototype and close with a
short list of what a real build would still need that the prototype
skipped — real data, persistence, auth, error handling, whatever applies.
Stop proposing changes after that.

When the user signals they want it built for real, turn the prototype
into a brief before anyone writes production code. Re-read the
prototype and everything the user said while playing with it, and
draft a proposed requirements list in three buckets: must-have,
nice-to-have, and cut. One short line per requirement, numbered, so the
user can accept, edit, or move any line by its number. Put the draft in
front of the user for approval — you propose, they decide — and do not
start implementation until they have. The approved list is the brief:
an implementing session must account for every line, and what is not on
the list is out of scope until someone adds it. When acceptance and
the build-for-real signal arrive in one message, fold what the gaps
list would have said into the draft's must-haves rather than sending
both.
