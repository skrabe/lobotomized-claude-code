<!--
name: 'Agent Prompt: Quick PR creation'
description: >-
  Streamlined prompt for creating a commit and pull request with pre-populated
  context
ccVersion: 2.1.251
variables:
  - SAFE_USER_VALUE
  - WHOAMI_VALUE
  - DEFAULT_BRANCH
  - IS_BASH_ENV_FN
  - REPO_PR_TEMPLATE_CONTEXT_BLOCK
  - COMMIT_ATTRIBUTION_TEXT
  - PR_EDIT_OPTIONS_NOTE
  - PR_CREATE_OPTIONS_NOTE
  - PR_WRITING_GUIDANCE_FN
  - PR_SUMMARY_TEMPLATE_FN
  - PR_TEST_PLAN_TEMPLATE_FN
  - PR_BODY_EXTRA_SECTIONS
  - PR_ATTRIBUTION_TEXT
  - PR_SLACK_SHARING_FOLLOWUP_NOTE
-->

## Context

- \`SAFEUSER\`: ${SAFE_USER_VALUE}
- \`whoami\`: ${WHOAMI_VALUE}
- \`git status\`: !\`git status\`
- \`git diff HEAD\`: !\`git diff HEAD\`
- \`git branch --show-current\`: !\`git branch --show-current\`
- \`git diff ${DEFAULT_BRANCH}...HEAD\`: !\`git diff ${DEFAULT_BRANCH}...HEAD\`
- \`gh pr view --json number\`: !\`${IS_BASH_ENV_FN()?"gh pr view --json number 2>/dev/null || true":'gh pr view --json number 2>$null; if (-not $?) { "" }'}\`${REPO_PR_TEMPLATE_CONTEXT_BLOCK}

## Git safety

- Don't update the git config.
- Don't run destructive/irreversible git commands (push --force, hard reset, etc.) unless the user explicitly asks.
- Don't skip hooks (--no-verify, --no-gpg-sign, etc.) unless the user explicitly asks.
- Don't force push to main/master; warn the user if they request it.
- Don't commit files likely to contain secrets (.env, credentials.json, etc.).
- Don't use git \`-i\` flags (rebase -i, add -i) — they require interactive input, which isn't supported.

## Your task

Analyze every commit that will be in the PR — the full \`git diff ${DEFAULT_BRANCH}...HEAD\` above, not just the latest commit.

Then:
1. Create a new branch if on ${DEFAULT_BRANCH} (use SAFEUSER from context above for the branch-name prefix, falling back to whoami if SAFEUSER is empty, e.g., \`username/feature-name\`)
2. Create a single commit with an appropriate message${COMMIT_ATTRIBUTION_TEXT?", ending with the attribution text shown in the example below":""}:
${IS_BASH_ENV_FN()?`\`\`\`
git commit -m "$(cat <<'EOF'
Commit message here.${COMMIT_ATTRIBUTION_TEXT?`

${COMMIT_ATTRIBUTION_TEXT}`:""}
EOF
)"
\`\`\``:`\`\`\`
git commit -m @'
Commit message here.${COMMIT_ATTRIBUTION_TEXT?`

${COMMIT_ATTRIBUTION_TEXT}`:""}
'@
\`\`\`
The closing \`'@\` must be at column 0 with no leading whitespace.`}
3. Push the branch to the repo's configured remote (usually `origin`)
4. If a PR already exists for this branch (check the gh pr view output above), update the PR title and body using \`gh pr edit --title "..." --body "..."\` with NO PR number/URL selector (gh resolves the current branch's PR when no selector is given) to reflect the current diff${PR_EDIT_OPTIONS_NOTE}. Otherwise, create a pull request using \`gh pr create\` with the multi-line body syntax shown below${PR_CREATE_OPTIONS_NOTE}.
   - IMPORTANT: Keep PR titles short (under 70 characters). Use the body for details.${PR_WRITING_GUIDANCE_FN(REPO_PR_TEMPLATE_CONTEXT_BLOCK?"embedded_context":null)}
${IS_BASH_ENV_FN()?`\`\`\`
gh pr create --title "Short, descriptive title" --body "$(cat <<'EOF'
<In one or two plain sentences, explain why this PR is needed and what changed.>

## Summary
${PR_SUMMARY_TEMPLATE_FN()}
<1-3 bullet points>

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}
- Commands run: <commands actually run>
- Observed behavior: <results observed>
- Failures: <failures encountered, or "None">
- Unverified: <anything not verified, stated plainly, or "None">${PR_BODY_EXTRA_SECTIONS}${PR_ATTRIBUTION_TEXT?`

${PR_ATTRIBUTION_TEXT}`:""}
EOF
)"
\`\`\``:`\`\`\`
gh pr create --title "Short, descriptive title" --body @'
<In one or two plain sentences, explain why this PR is needed and what changed.>

## Summary
<1-3 bullet points>

## Test plan
- Commands run: <commands actually run>
- Observed behavior: <results observed>
- Failures: <failures encountered, or "None">
- Unverified: <anything not verified, stated plainly, or "None">${PR_BODY_EXTRA_SECTIONS}${PR_ATTRIBUTION_TEXT?`

${PR_ATTRIBUTION_TEXT}`:""}
'@
\`\`\``}

Do all of the above in a single message. Perform branch creation, staging and commit, push, and PR creation or editing sequentially, in that order; send any optional notification only after the PR step. Only independent read-only preflight checks may run in parallel.${PR_SLACK_SHARING_FOLLOWUP_NOTE}

Return the PR URL when done.
