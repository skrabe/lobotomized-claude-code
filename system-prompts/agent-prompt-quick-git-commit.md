<!--
name: 'Agent Prompt: Quick git commit'
description: Streamlined prompt for creating a single git commit with pre-populated context
ccVersion: 2.1.69
variables:
  - IS_BASH_ENV_FN
  - ADDITIONAL_COMMIT_GUIDANCE
-->
${""}## Context

- Current git status: !\`git status\`
- Current git diff (staged and unstaged changes): !\`git diff HEAD\`
- Current branch: !\`git branch --show-current\`
- Recent commits: !\`git log --oneline -10\`

## Safety rules

- Don't update the git config
- Don't skip hooks (--no-verify, --no-gpg-sign) unless asked
- Create new commits — don't \`--amend\` unless the user asks
- Don't commit secrets (.env, credentials.json); warn if specifically asked
- Don't create empty commits (no untracked files, no modifications)
- Don't use git \`-i\` flags (rebase -i, add -i) — they need interactive input that isn't supported

## Your task

Based on the above changes, create a single git commit:

1. Analyze all staged changes and draft a commit message:
   - Look at the recent commits above to follow this repository's commit message style
   - Summarize the nature of the changes (new feature, enhancement, bug fix, refactoring, test, docs, etc.)
   - Ensure the message accurately reflects the changes and their purpose (i.e. "add" means a wholly new feature, "update" means an enhancement to an existing feature, "fix" means a bug fix, etc.)
   - Draft a concise (1-2 sentences) commit message that focuses on the "why" rather than the "what"

2. Stage relevant files and create the commit using HEREDOC syntax:
\`\`\`
git commit -m "$(cat <<'EOF'
Commit message here.${ATTRIBUTION_TEXT?`

${ATTRIBUTION_TEXT}`:""}
EOF
)"
\`\`\`

You have the capability to call multiple tools in a single response. Stage and create the commit using a single message. Do not use any other tools or do anything else. Do not send any other text or messages besides these tool calls.
