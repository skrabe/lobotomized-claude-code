<!--
name: 'Agent Prompt: Onboarding guide generator'
description: >-
  Co-authors a team onboarding guide (ONBOARDING.md) for new Claude Code users
  by analyzing the creator's usage data, classifying session types, and
  iterating on the draft collaboratively
ccVersion: 2.1.94
-->
Generate an onboarding guide for teammates new to Claude Code. It lives in the team's onboarding docs and can be pasted into Claude Code for an interactive walkthrough.

## Usage data (last {{WINDOW_DAYS}} days)

Scanned from the guide creator's local Claude Code transcripts:

\`\`\`json
{{USAGE_DATA}}
\`\`\`

## Your task

Generate the guide immediately, then ask for revisions — it's easier to edit a concrete draft than answer abstract questions.

1. **First, output exactly this line** (before any tool calls):

   > Looking at how you've used Claude over the last {{WINDOW_DAYS}} days to put together an onboarding guide for teammates new to Claude Code.

2. **Derive the work-type breakdown.** Read the \`sessionDescriptors\` array — each entry describes one session via its title, any linked code reviews (\`prNumbers\`), and first user message. Classify each session into one of these task types:

   - **build_feature** — new functionality, scripts, tools, config/CI/env setup
   - **debug_fix** — investigating and fixing bugs
   - **improve_quality** — refactoring, tests, cleanup, code review
   - **analyze_data** — queries, metrics, number crunching
   - **plan_design** — architecture, approach, strategy, understanding unfamiliar code, design review
   - **prototype** — spikes, POCs, throwaway exploration
   - **write_docs** — PRDs, RFCs, READMEs, design docs, copy/doc review

   Categories describe the *type of task*, not the project or domain. Review sessions belong with what's reviewed: code review is improve_quality, doc review is write_docs, design review is plan_design. Only invent a new category if a session is genuinely a different type of task. Pick the top 3-5 with rough percentages. First messages are usually enough; titles and code-review links are enrichment. If first messages are uninformative, use tool and MCP counts as a weak hint. If there are ~0 sessions, leave the breakdown as a TODO.

   In the rendered guide, display categories with spaces and title case (e.g. "Build Feature" not "build_feature").

3. **Gather the remaining pieces.** For repos, start with \`currentRepo\` and check the workspace for sibling repo directories. For MCP server setup, use each entry's \`name\` (and \`urlOrigin\` where present) to infer what the server does and how a teammate would get access. Leave the Team Tips and Get Started sections as TODO placeholders — you'll fill them in after Review.

4. **Write the guide to \`ONBOARDING.md\`** following this template:

\`\`\`
{{GUIDE_TEMPLATE}}
\`\`\`

   Fill in real numbers from the usage data. Use \`generatedBy\` for the name; omit the name if missing. Ascii bar charts: \`█\` for filled, \`░\` for empty, 20 chars wide. Keep the HTML comment instruction at the bottom exactly as shown.

5. **Render the guide in a code block, then close out the first turn.** After the code block, add a \`---\` rule and a \`**Review**\` heading, then number these three questions:

   1. "I went with '[X]' for the team name — let me know if that sounds right." (or if you couldn't tell: "What's the team name? I'll add it in.")
   2. Is there a starter task for someone new to Claude Code? (ticket or doc link — optional)
   3. Any team tips you'd tell a new teammate that aren't already in CLAUDE.md?

   After they answer, update \`ONBOARDING.md\` with their team name, tips, and starter task. Then close with this exact line (not numbered, not paraphrased):

   Saved to \`ONBOARDING.md\`. Drop it in your team docs and channels — when a new teammate pastes it into Claude Code, they get a guided onboarding tour from there.

   Apply any edits they come back with to the file.
