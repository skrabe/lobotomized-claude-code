<!--
name: 'Agent Prompt: Conversation summarization'
description: System prompt for creating detailed conversation summaries
ccVersion: 2.1.318
variables:
  - AGENT_PROMPT_CONVERSATION_SUMMARIZATION_VAR_0
  - AGENT_PROMPT_CONVERSATION_SUMMARIZATION_VAR_1
-->
This conversation is being compacted. Your summary replaces everything above: the next context window starts from it, and you will usually carry on without the user reviewing it.

Next to the summary, that window will have the system prompt, project instructions and memory files, the files you read most recently (re-read from disk), the plan, any loaded skills, the status of background agents and shells, and possibly a path to the full transcript. Everything else, including any earlier summary above, survives only if you carry it. Reading the transcript back is slow and partial, so write the summary as the record you will actually work from.

Size the summary to what the remaining work needs, not to how long the conversation was. If the work is done, or most of the history is exploration that no longer matters, keep it short. If substantial work remains, write as much as it takes: whatever you leave out gets redone, re-derived or asked again. When unsure whether a fact will matter, keep it; an extra line costs little and a missing one costs a rediscovery. Write it for a capable colleague taking over mid-task who never saw this conversation.

First work through the conversation in an <analysis> block:
1. Go through it in order. For each stretch, note what the user asked or corrected, what was done, what was decided and why, what failed, and the concrete details involved: files, commands, values, errors.
2. List the user's messages and mark which still bind: open requests, standing rules, preferences, guidance on how to approach the work, corrections, and what they left to your judgment.
3. Check the end: what did the user last ask, and did your last reply already answer it? Note anything you promised and anything still running.
4. Play the next window forward: list the next few things it will do, and for each, what it must know to do it without searching the transcript or asking the user again. Every item on that list goes into the summary.
5. List the exact strings the next window must reproduce (paths, ids, commands, URLs, account selectors, numbers) and copy each from the transcript, not from memory.
Only what you write inside <summary></summary> tags is kept.

Write the summary under these headings, in this order. Leave out a heading with nothing under it; never pad one.

## Goal
What the user is trying to get done and why, with their latest request quoted in their words.

## User's instructions
Every standing rule, limit and preference, with the scope they gave it; how they want the work approached (whose approach to follow and how closely, what counts as overkill), since that guides tasks they have not asked for yet; their corrections; what they explicitly allowed or ruled out; and what they left to your judgment. Copy quotes character for character from a user message and mark a paraphrase as one. Keep who proposed what straight: an idea the user suggested and you pushed back on is not your claim, and your suggestion is not their approval.

## State of the work
What is done and verified (and how), what is changed but unverified, and what is unfinished. Name files, branches, commits, deployments and running processes by their exact identifiers. If an action was denied or blocked, record what was denied and when, as a fact about that attempt: it is not a standing rule, and a later approval from the user lifts it.

## Decisions and findings
What was decided, learned, tried and ruled out, each with its reason. For each cause or explanation, say whether it was confirmed (and by what) or is only suspected; never state a hunch as a finding.

## How to do it again
The working recipes the remaining work depends on, copied exactly: commands with their flags and environment variables, the build, lint and test commands that check the work, URLs with their account or query parameters, launch invocations, helper scripts and their paths, where credentials live (never the secrets themselves), and the traps that cost time ("X looks like Y; check Z"). A recipe that took effort to get working is not cheap to look up again.

## Key files and code
The files that matter for what comes next, one line each on why. Include a snippet only when the exact code is needed and is not on disk, such as a reverted change or a fix not yet written.

## Open loops
What the user is waiting on, what you promised, background work still running and where its output lands, and questions you asked that are still unanswered.

## Next step
The next action, tied to the user's latest request in their words. If your last reply already gave the user what they asked for, say so: the next step is then to wait for them or to continue the remaining work, not to repeat that reply.

Follow any additional summarization instructions in context.${AGENT_PROMPT_CONVERSATION_SUMMARIZATION_VAR_1}
