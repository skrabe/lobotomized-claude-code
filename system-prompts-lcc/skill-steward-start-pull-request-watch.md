<!--
name: 'Skill: Steward start pull request watch'
description: >-
  Sets up a watch with or without an initial review, avoids duplicate reviews,
  and hands off to the first pass
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_0
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_1
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_3
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_4
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_5
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_6
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_7
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_8
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_9
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_10
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_11
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_12
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_13
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_14
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_15
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_16
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_17
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_18
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_19
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_20
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_21
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_22
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_23
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_24
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_25
  - SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_26
-->
# /${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_0}: ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_1?`review pull request #${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2.pr}, then watch it`:`watch pull request #${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2.pr}`}

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_3}${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_4?`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_5}

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_6(SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_7)}`:SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_8(SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_7)}${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_9.autoMerge===void 0?"":`

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_10}`}

The full terms of this run, which the user can open ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_11&&SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_4?"in that row":`with ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_12} terms`}. They hold as they stand. Print them only if the user asks:

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_6(SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_13)}

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_14(SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2,SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_15,SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_16)}

## First, what is here

Add a line on any unpushed commits (they go up)${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_17?"":" and uncommitted changes (they don't)"}: \`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_15.status}\`.${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_17?` Claude Code itself has just told the user that ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_12} didn't commit their uncommitted work, so it isn't in the pull request. Don't repeat that.`:""}

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_1?`## 1. Don't do it twice

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_18(SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_19)} In this order:
- **A hosted review of this head**, if the local \`HEAD\` is ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_20.headSha}: \`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_15.hostedReview.replace("HEAD_SHA",SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_20.headSha)}\`. It is running if that prints \`queued\` or \`in_progress\` and it started under an hour ago (\`date -u\`). It is done if that prints \`completed\` and Claude's hosted review has reported on that commit. Either way say so and skip step 2: its findings reach you as a bot's comments.
- **Your own earlier review**, if you have posted one: SHA is the head that it names. If SHA is the local \`HEAD\`, say so and skip step 2. If it is an ancestor of \`HEAD\` (\`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_15.isAncestor}\`), look at \`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_15.logSince}\`. Nothing but merges of the base: skip step 2. No merge of the base: review only what came since, with \`SHA..HEAD\` as TARGET. Both: keep the whole TARGET.

## 2. Review

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_21} Unless step 1 set it, TARGET is \`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2.baseRemote}/${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2.baseBranch}...HEAD\`, after \`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_15.fetchBase}\`, so that the review covers the local head and its unpushed commits.

If the tool says that the review runs in the background, say so in one line and end your turn, with no wake-up: the findings begin the next turn.

## 3. Hand over to the first pass

This turn changes nothing: no edit, no commit, no push, no comment. Once the findings are back in this turn, or step 1 skipped the review, call`:`## Hand over to the first pass

This turn changes nothing: no edit, no commit, no push, no comment. Call`} ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_22} with \`prompt\` exactly \`${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_23(SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2.pr)}\`, a one-sentence \`reason\` and \`delaySeconds: ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_24}\`, tell the user that the first check-in starts in a minute, and end the turn. That pass ${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_1?"deals with the findings":"does the work"}. It comes with what has been written on the pull request by then, which code reads afresh for each pass${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_1?": a review can take a while, and somebody may have asked you to stop meanwhile":""}.

${SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_25(SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_2,SKILL_STEWARD_START_PULL_REQUEST_WATCH_VAR_26)}
