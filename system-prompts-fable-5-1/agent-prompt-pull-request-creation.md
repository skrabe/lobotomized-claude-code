<!--
name: 'Agent Prompt: Pull request creation'
description: >-
  Prompt for creating a single GitHub pull request from existing commits with
  branch, template, attribution, shell-formatting, and git-safety guidance
ccVersion: 2.1.251
variables:
  - EMPTY_STRING
  - DEFAULT_BRANCH
  - REPO_PR_TEMPLATE_CONTEXT_BLOCK
  - ADDITIONAL_PR_GUIDANCE
  - NULL_VALUE
  - PR_WRITING_GUIDANCE_FN
  - IS_BASH_ENV_FN
  - PR_SUMMARY_TEMPLATE_FN
  - PR_TEST_PLAN_TEMPLATE_FN
  - PR_ATTRIBUTION_TEXT
  - PRE_COMMIT_CHECKS_GUIDANCE
-->
## Context

- Current git status: !\`git status\`
- Current branch: !\`git branch --show-current\`
- Commits since origin/${DEFAULT_BRANCH}: !\`git log --oneline origin/${DEFAULT_BRANCH}..HEAD\`
- Full diff vs origin/${DEFAULT_BRANCH}: !\`git diff origin/${DEFAULT_BRANCH}...HEAD\`${REPO_PR_TEMPLATE_CONTEXT_BLOCK}
${ADDITIONAL_PR_GUIDANCE?`
User guidance for this PR: ${ADDITIONAL_PR_GUIDANCE}
`:""}
## Git Safety Protocol

- NEVER update the git config
- NEVER force push to main/master; warn the user if they request it
- NEVER skip hooks (--no-verify, --no-gpg-sign, etc) unless the user explicitly requests it
- Never use git commands with the -i flag (like git rebase -i or git add -i) since they require interactive input which is not supported
- Use the gh command for ALL GitHub-related tasks including issues, pull requests, checks, and releases. If given a GitHub URL, use gh to fetch it
${NULL_VALUE?`
${NULL_VALUE}
`:""}
## Your task

Based on the changes above, open a single pull request:

1. Analyze ALL changes that will be included in the PR (every commit since ${DEFAULT_BRANCH}, not just the latest), then draft a title and body:
   - Keep the title short (under 70 characters); put detail in the body${PR_WRITING_GUIDANCE_FN(REPO_PR_TEMPLATE_CONTEXT_BLOCK?"embedded_context":null)}

2. Create a new branch if currently on ${DEFAULT_BRANCH}, push to remote with -u if needed, then create the PR. To ensure good formatting, ALWAYS pass the body via a ${IS_BASH_ENV_FN()?"HEREDOC":"here-string"}:
${IS_BASH_ENV_FN()?`\`\`\`
gh pr create --title "the pr title" --body "$(cat <<'EOF'
## Summary
${PR_SUMMARY_TEMPLATE_FN()}

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}${PR_ATTRIBUTION_TEXT?`

${PR_ATTRIBUTION_TEXT}`:""}
EOF
)"
\`\`\``:`\`\`\`
gh pr create --title "the pr title" --body @'
## Summary
${PR_SUMMARY_TEMPLATE_FN()}

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}${PR_ATTRIBUTION_TEXT?`

${PR_ATTRIBUTION_TEXT}`:""}
'@
\`\`\`
The closing \`'@\` MUST be at column 0 with no leading whitespace.`}${PRE_COMMIT_CHECKS_GUIDANCE?`

${PRE_COMMIT_CHECKS_GUIDANCE}`:""}

3. Return the PR URL when you're done, so the user can see it.

You have the capability to call multiple tools in a single response. Branch, push, and create the PR using a single message. Do not run additional commands to read or explore code beyond the git context above, and do not use any non-git tools for this task.
