<!--
name: 'Data: classifiers'
description: >-
  claude-approvals skill reference file on custom classifiers, read by the model
  after SKILL.md.
ccVersion: 2.1.332
-->
# Claude Approvals: custom classifiers

A reference file of the skill \`claude-approvals\`. Read \`SKILL.md\` first: everything there above "Workflow" binds here too. A section named in quotation marks that this file lacks stands there. \`SKILL.md\` and \`references/...\` count from the skill's folder, not from the repository.

**Contents:** Custom classifiers; Write one, step by step; Keys of def.yml; Outputs; Inputs; Tools and findings; The prompt; Recommendations; How a rule reads it; When it runs; No result; Cheaper and faster; Monorepos, names and versions; Changing a live classifier; A fuller classifier.

## Custom classifiers

A custom classifier is a Claude run that answers the repository's own question about a pull request. It gives **outputs**: results that a policy reads. Rules read the result as \`repo/<name>\`. With \`tools\` it can also report **findings** (problems for people to read), comment, set labels or add reviewers. To change the policy file beyond wiring the classifier in, follow \`SKILL.md\`.

| In \`.claude/classifiers/<name>/\` | What it is |
|---|---|
| \`def.yml\` (or \`def.yaml\`, never both) | The definition: what the classifier answers and what it may do. This one file can be the whole classifier. |
| \`prompt.md\` | What to look for. It is optional: the prompt can stand in \`def.yml\` instead, under \`prompt\`. |
| any other text file | Reference text that the prompt names (see "The prompt"). |
| the folder's name | The classifier's name: lower-case letters, digits and \`_\`, at most 64 characters. \`scales\` is taken. |

## Write one, step by step

1. **Ask first whether a classifier is needed.** If \`paths\` or a fact can say it, write a rule and no classifier (\`SKILL.md\`): a rule is free, and no author's text can steer it. "Add the security team when auth code changes" is such a rule: those \`paths\`, and \`seats: [{ count: 1, from: [acme/security] }]\`. Say two things of it. It makes the team's approval required, but adds nobody as a reviewer on GitHub and notifies nobody: \`CODEOWNERS\` does that, or the \`reviewers\` tool. And a member's own pull request fills the seat by itself: \`from: [acme/security, "!pr/authors"]\` leaves authors out. Working alone, write the set with that item, unless it would lock.
2. **Settle the question and its possible results with the user.** Use a few distinct words (\`pass\`/\`fail\`, \`low\`/\`medium\`/\`high\`), and decide which result is safe in doubt.
3. **Write \`.claude/classifiers/<name>/def.yml\`.** Start from a starter below: \`change_risk\` for a rating, \`ledger_check\` for a yes-or-no question. Follow "Recommendations".
4. **Wire it in**, now or after the trial in step 7. A definition alone runs nothing: a rule whose \`paths\` match must name it. Keep the strict verdict as the rule's own, and read the classifier in overrides that ask for less on a result. For a classifier that gates nothing, see "To flag only".
5. **Decide what no result means** (see "No result").
6. **Say what it costs.** Each pull request that a naming rule matches mostly pays for up to one run at each new patchset (see "When it runs"), and for one more for each value of an input that no \`merge\` joins (see "Inputs"). After an error or a temporary fault, Claude Approvals can start the run again by itself, more than once, billed like any other: promise no number of runs. Runs are billed by tokens to the Claude organization's usage credits, in observe mode and under \`advisory\` too. \`budget\` stops a run at about 10 US dollars by default, and spend can pass that. No typical price of a run is known: give none.
7. **Offer a trial.** Add \`advisory: [repo/<name>]\` to the rule that already matches, keeping the names it already lists there or gets through \`use\`. The classifier runs there and is paid for, but is not waited for and decides nothing.
   - On an enforced rule, this draws the warning "rules still hold on these files, but the check cannot tell that they ask as much as this rule did". It is expected here: say so.
   - To try it on a few paths only, add a rule with three keys and no \`verdict\`: \`purpose\`, \`paths\` and \`advisory\`. Such a rule changes no approval: it asks nobody, but for the one person that a protected file always takes. It runs the classifier only on files that a rule with a \`verdict\` matches too, or on a protected file it matches where a policy file above has one.
   - The trial starts once the edit is merged, and Claude Approvals can go on reading the earlier copy for about five minutes. After that, open a pull request that is no draft and changes a matching file.
   - The result shows in Claude Approvals' comment, in the part titled "Classifier results", or in the check's summary, in the part titled "Advisory classifiers (not counted toward this verdict)". It comes at the first evaluation after the run ends. An approval or a request for changes starts one; a review with only comments does not. Until then the line reads "no result recorded yet".
   - While the policy file says \`mode: observe\`, it gates nothing, so the name can go straight into an override's \`if\`. A comment, labels and reviewers cannot be tried there (see "In observe mode").
   - If it should gate, move the name into an override's \`if\` after a few runs. Where the policy reads Code Review at no set \`level\`, say what that costs: once any \`if\` reads your classifier, a pull request whose review Code Review declines, or a rerun drops, can stay red, whoever approves. Until then, enough people could pass it (\`references/tune.md\`).
   - To undo, take the name out of the rule: its findings close, and what it added comes off. The folder can stay.
8. **Check** ("Every edit, every reply"). The folder and the rule can go in one pull request: the check reads the two together. In a large monorepo, it may ask for the classifier and each directory's policy file in pull requests of their own: then merge the classifier first, and update the policy file's branch.

\`\`\`yaml
# .claude/classifiers/change_risk/def.yml
version: 1
description: "How risky is this change to ship?"
model: opus
prompt: |
  Rate how risky this change is to ship.
  high: it touches sign-in, billing or a data migration.
  medium: it changes behavior a user can see.
  low: anything else. When two fit, pick the higher.
outputs:
  risk: { type: ordinal, values: [low, medium, high] }
\`\`\`

\`\`\`yaml
# .claude/approvals.yml: a sample, not the user's file
version: 1
mode: observe
rules:
  - purpose: "Two people. One when Claude's review passes. Nobody when it passes and the risk is low."
    paths: ["**"]
    verdict: { claude: comments, seats: 2 }
    override:
      - { if: "claude/code_review = pass AND repo/change_risk = low", verdict: { claude: approves, seats: 0 } }
      - { if: "claude/code_review = pass", verdict: { claude: approves, seats: 1 } }
  - purpose: "A change to the review rules or to a classifier takes two people."
    paths: ["**/.claude/**", "**/REVIEW.md", "**/.gitattributes", "**/.gitmodules"]
    nested: inherit
    verdict: { claude: comments, seats: 2 }
\`\`\`

The sample observes, as a new policy file should. In the user's file, keep the user's own \`mode\` line. Once it enforces, the last rule keeps its four paths at two people. Files outside them, such as \`CODEOWNERS\`, have no such rule here: on a pass their author alone is enough, and Claude approves. A bot's pull request also needs nobody, on a pass and a low rating.

Once it enforces, this sample carries four risks:

- A run reads text that the pull request's author wrote, and that text can try to steer the result. Here a steered \`low\` beside a passed review lets nobody look. On paths that matter, ask for people whatever a classifier says.
- GitHub can count Claude's approval as one that it requires. So \`seats: 0\` can let nobody look, and \`seats: 1\` can let the author merge alone.
- GitHub may require approvals while neither "Dismiss stale pull request approvals when new commits are pushed" nor "Require approval of the most recent reviewable push" is on. Then GitHub goes on counting Claude's approval after a later push until Claude Approvals withdraws it, which can come late, or not at all. Unreviewed code can merge on it meanwhile.
- An \`if\` here reads your classifier beside Code Review. So a pull request whose review Code Review declines, or a rerun drops, can stay red, whoever approves (\`references/tune.md\`).

Tell the user all four. Recommend the required check and one of the two settings, which only an admin can turn on (\`SKILL.md\`).

**The starter for a yes-or-no question** is a team's own classifier, beside the team's own policy file. The prompt sends every doubt to \`fail\`, and the rule's own verdict is what a \`fail\` or no result gets:

\`\`\`yaml
# services/billing/.claude/classifiers/ledger_check/def.yml
version: 1
description: "Does this change keep the ledger balanced?"
model: opus
prompt: |
  pass: every change to a balance writes a matching entry to the ledger.
  fail: anything else, or you cannot tell.
outputs:
  result: { type: criteria, values: [pass, fail] }
\`\`\`

\`\`\`yaml
# services/billing/.claude/approvals.yml
version: 1
mode: observe
rules:
  - purpose: "Billing requires two team members, or one (even the author) when the ledger check passes."
    paths: ["**"]  # paths start at services/billing/
    verdict: { claude: comments, seats: [{ count: 2, from: acme/billing }] }
    override:
      - if: "repo/ledger_check = pass"
        verdict: { seats: [{ count: 1, from: acme/billing }] }
\`\`\`

In the root's file, the same rule on \`services/billing/**\` would change nothing while a rule on \`"**"\` asks for more there ("How a policy decides", point 1). A run reads the author's text, so a steered \`pass\` leaves a team member's own change with nobody else looking: say so, and recommend \`from: [acme/billing, "!pr/authors"]\` in the override.

**To block until a result comes,** make \`blocks\` the rule's own verdict, and open it in an override, which must then write \`seats\` too. With one policy file, put the folder and this rule in the root: a block holds beside a rule on \`"**"\`.

\`\`\`yaml
# in services/billing/.claude/approvals.yml: one more rule
  - purpose: "A change to payouts is blocked until the ledger check passes. Then it takes two team members."
    paths: ["payouts/**"]
    verdict: { claude: blocks }
    override:
      - { if: "repo/ledger_check = pass", verdict: { claude: comments, seats: [{ count: 2, from: acme/billing }] } }
\`\`\`

Under \`mode: observe\` nothing is blocked yet: say so (to go live, follow \`SKILL.md\`). Once the file enforces, the check stays red on a \`fail\` or no result, whoever approves. Say the ways out: a push that mends the change, \`@claude approvals rerun\` by a person with write access, or an edit of the policy file, merged in a pull request of its own, which the blocked one meets when it is next judged. Keep the rule's \`paths\` off \`.claude/\`: a rule that reaches the policy file blocks that edit too, and then only someone who may bypass the branch rules can merge it.

**To flag only,** and gate nothing, grant \`findings\`, write no \`outputs\`, and name the classifier under \`advisory\` in a rule with no \`verdict\`. That rule is the finished wiring, not only a trial:

\`\`\`yaml
# .claude/classifiers/migration_flags/def.yml
version: 1
description: "Which steps of this database migration are risky?"
model: sonnet
tools: [findings]
prompt: |
  Report each risky step of a database migration as a finding, on its line, titled by the kind of step and its table.
  The risky steps: a dropped column or table, a rewrite of a large table, a lock that blocks writes.
  Use severity high where data can be lost, and medium otherwise.
  Leave an earlier finding open while its step stands, and resolve it once a later push takes the step out or makes it safe.
\`\`\`

\`\`\`yaml
# in .claude/approvals.yml: one more rule
  - purpose: "Flag risky database migrations. This rule asks nobody."
    paths: ["**/migrations/**"]
    advisory: [repo/migration_flags]
\`\`\`

It starts the classifier only for a changed file that a rule with a \`verdict\` matches too, or for a protected file that it matches where a policy file above that file has a rule with a \`verdict\`: a pull request with neither brings no run, and no warning says so. The classifier's findings are shown and decide nothing. They open ordinary review threads: where the branch rules require conversations to be resolved, somebody must resolve them on GitHub before the merge. \`comment\` serves too, but only under an enforced rule (see "In observe mode").

## Keys of def.yml

| Key | Required | Takes |
|---|---|---|
| \`version\` | yes | the bare number \`1\` |
| \`description\` | yes | one line, at most 1,000 characters |
| \`model\` | yes | a lower-case family (\`opus\`, \`sonnet\`, \`haiku\`, \`fable\`), or the exact Claude API ID of a generally available model; either may end in \`-fast\` |
| \`prompt\` | this or \`prompt.md\`, not both | text |
| \`outputs\`, \`inputs\` | no | maps of names |
| \`tools\` | no | a list of \`findings\`, \`comment\`, \`labels\`, \`reviewers\`, \`code\` |
| \`budget\` | no | \`{ time, cost }\`, each optional: whole seconds, whole US dollars, or \`infinite\`; default 600 and 10 |

- A key that Claude Approvals does not read refuses the definition, so add none that this table lacks. The classifier then reads \`error\` until the file is fixed. Where the person names such a key, leave it out and say that it will most likely refuse the definition. There is no \`name\` key, and no \`type\` on an input.
- **The file** is YAML, and comments are allowed. Some confusing YAML only draws a warning. \`def.yml\` holds at most 64 KiB, \`prompt.md\` at most 512 KiB, and a list or a map at most 64 entries. Both are plain files of the repository: write no token or password into them.
- **\`description\`** is shown beside the result in the check and the comment, cut at 200 bytes. One that holds \`#\`, \`&\`, \`*\`, \`<\`, \`>\`, \`@\`, a vertical bar, an emoji, an arrow or a bot's command is not shown at all, and usually draws a warning. Keep it short and plain.
- **\`model\`:**
  - A family follows its newest model. It is looked up as each run starts, so cost and results can change with no pull request, and with them who must approve. Results already given stand.
  - An exact ID changes only by a commit, and stops loading once its model is retired. It must be of version 4.6 or later.
  - Say which of the two you wrote. \`latest\` and a family in capitals are refused. If you infer an ID, say so and ask the user to confirm it.
  - Where the Claude organization keeps a list of allowed models and the model is not on it, no run starts, and the classifier reads \`error\`.
  - \`-fast\` at the end (\`opus-fast\`, \`claude-opus-5-5-fast\`) asks for fast mode, at a higher price per token, so a run reaches its \`cost\` sooner. Where the model has no fast mode, or the organization has it off, the run goes at standard speed, and a pull request that changes the definition usually draws a warning. Write it only where the user asks for speed, and say that it costs more.
- **\`budget\`** stops one run. \`infinite\` asks for the most that the organization is allowed.
  - \`time\` goes up to 3,600 (\`infinite\` asks for that). \`cost\` goes up to 10. A number above its limit is cut to the limit, with a warning, so a \`cost\` above 10 changes nothing. Zero is refused.
  - A \`time\` above the default can keep the check in progress about that long: say so. It is a ceiling, not a promise. Keep it under about 1,100: from about 1,130, the definition draws a warning, and the run may be restarted, or show as an error until it reports. A \`time\` under 60 draws a warning too.

## Outputs

| \`type\` | Result | Needs | Operators |
|---|---|---|---|
| \`criteria\` | one word, no order | \`values\` | \`=\`, \`!=\` |
| \`ordinal\` | one word, **least first** | \`values\` | all six |
| \`numeric\` | a whole number | \`min\`, \`max\`: the lowest and the highest result | all six |

- Each output needs a \`type\`, and may have a \`description\`. Every run must answer every output.
- With no \`outputs\`, a condition can read only \`.severity\`, \`= error\` and \`= incomplete\`. That suits a classifier that only flags, comments or sets labels.
- No free text: for prose, grant \`tools: [comment]\` or \`[findings]\`.
- With several outputs, name one: \`repo/release_check.kind = docs\`. With one, the name alone reads it.
- Words: lower case, digits and \`_\`, not starting with \`_\`. Quote \`"yes"\` and \`"no"\`.
- Refused words: \`true\`, \`false\`, \`error\`, \`incomplete\`, \`complete\`.
- Refused output names: \`severity\`. A name that starts with \`_\` is refused too.

## Inputs

An input lets a rule adjust the classifier. Write an input like this: \`inputs: { rigor: { values: [quick, thorough], merge: right, default: quick } }\`. A condition gives it in parentheses after the name, which makes a **call**: \`"repo/change_risk(rigor=thorough) < high"\`.

- An input is words (\`values\`, the words that a rule may write) or a whole number (\`min\` and \`max\` in place of \`values\`). It is never free text, and \`unset\` cannot be one of its words. It may have a \`description\`.
- \`default\` is required. It is one word of \`values\`, or a number from \`min\` to \`max\`. A run gets it where a call does not give the input, and the name alone takes every \`default\`.
- \`merge\` says what happens where calls ask for different values:

| \`merge\` | Calls that differ become |
|---|---|
| \`right\` | one run, with the word later in \`values\` |
| \`left\` | one run, with the earlier word |
| \`list\` | one run, with every word asked for. Only here may a call or the \`default\` be a list: \`repo/scan(scope=[prod, sec])\` |
| \`max\`, \`min\` | for a number: one run, with the larger or the smaller |
| \`unset\`, the default | a run each |

- With no \`merge\`, each different value is a separate paid run, with its own result. It has its own \`.severity\` too. Give every input a \`merge\` unless separate results are wanted.
- List \`values\` from lightest to most thorough and write \`merge: right\` (\`max\` for numbers).
- Under \`left\` or \`min\` the lightest value asked for wins, and a bare name in another matching rule asks for the default. Nothing warns: prefer \`right\` or \`max\`.
- Calls are merged before anything runs: those of every matching rule whose \`if\` the facts do not make false, under \`advisory\` too, and two in one rule. With several inputs, only calls that agree on every input under \`unset\` merge.
- A call gives a literal, or a local that holds one, never a fact or a classifier's result. The order of its inputs does not matter, and a \`default\` written out changes nothing. Write a call in quotes, under \`advisory\` and in a local too: unquoted, a comma inside \`[ ]\` or \`{ }\` splits it.

## Tools and findings

Every run can read the pull request with no entry at all: its title, description, author, changed files, diff and approvals, the reviewers asked for, the classifier's earlier runs, the policy files and the other files of its own folder. Each entry of \`tools\` grants one more thing:

| Entry | The run can |
|---|---|
| \`findings\` | report a finding, resolve or re-open one that the classifier reported earlier, and list those. Rules can then read \`.severity\`. Only with this entry can a run read the review threads |
| \`comment\` | keep one comment on the pull request, edited in place |
| \`labels\` | set a label, and swap or remove one that it set |
| \`reviewers\` | add a reviewer, and remove one that it added |
| \`code\` | read two read-only folders, \`head/\` and \`default/\` |

- **Name no tool in a prompt.** Say in plain words what the run should do, such as "report each risky step as a finding" or "resolve a finding once a later push fixes it". The run sees its own tools. Their names and inputs can change without notice, and a run that calls a tool by a name that it does not have gives no result. The five entries above are the format's own words: write those under \`tools\`. Where a prompt that you edit names a tool, offer to reword it.
- A tool that is not granted does not exist for the run. No entry grants a shell or network access. A classifier changes only what it added. A run may start sub-agents, which only read, and is told to start them only where its prompt asks.
- **On a pull request from a fork,** no classifier starts until a person with write access vouches for the commit, by a comment of \`@claude approvals rerun\` and its full SHA. There, and mostly where an author lacks write access, a run writes nothing on GitHub (no comment, label or thread, and no reviewer set there). The run's findings still count, with no thread to reply in. A reviewer that it adds is named in Claude Approvals' comment, and, where a rule's condition reads the classifier, the check still needs their approval, though on a fork that approval may never count ("Labels, reviewers and code", below).
- **In observe mode** a run keeps only \`findings\` and \`code\`. It posts no comment, and its findings are listed in Claude Approvals' comment, with no threads. That holds while only rules that observe name the classifier on the changed files.
- A rule **reaches** a classifier unless it reads it only below its first true override, or only in overrides while its own \`if\` is false. Once no matching rule reaches it, what it left is cleared: its findings are resolved, and its labels and added reviewers come off.

### Findings

A finding is one problem in the change. Reporting one is always optional.

| A finding has | Meaning |
|---|---|
| a title | A few words that name the problem. The same title on the same file in a later run is the same finding, so a second place in one file needs a title of its own, or a mention in the first one's text. |
| a text | What is wrong and what would fix it. |
| a severity | \`minimal\`, \`low\`, \`medium\`, \`high\` or \`critical\`. |
| a file (optional) | One that the pull request adds, edits or deletes. With it, the finding opens a review thread, whose footer names the classifier and the finding's ID. It can also name one line of that file, or a range, that the diff shows. Without it, the finding is about the whole change and stands in Claude Approvals' comment. |

- **\`.severity\`** is what a policy reads of findings: the worst finding that one run has open (\`none\`, \`minimal\`, \`low\`, \`medium\`, \`high\`, \`critical\`, with all six operators). An open finding changes the check only where an \`if\` reads it: elsewhere, as under \`advisory\`, it is only shown. With no result, \`.severity\` is still at least the worst finding that an earlier completed run left open.
- Read \`.severity\` as one more condition in an override that asks for less, or alone in a rule's first override that asks for more, such as \`{ if: "repo/change_risk.severity > medium", verdict: { claude: blocks } }\`. Such an override draws the warning "then decides, which is looser in this field". It is expected: where the run has no result, the override can be skipped, and the rule's own verdict decides. Say so, and say the way out of a wrong finding, which the next point gives.
- **A finding stays open** until a later run of its classifier or a person on the policy's \`findings\` lists resolves it, its file leaves the pull request, or no matching rule reaches the classifier. A run may close its own findings under any list, \`nobody\` too. By default the lists hold nobody: no person's resolve closes a finding, and no reply in its thread counts for the run. A finding with no thread closes only by a comment of \`@claude approvals resolve\` with its ID (\`references/explain.md\`). A person's close lasts even if the list or their access changes later.

**Who may close a finding:** \`findings: { resolution: { repo/change_risk: [acme/leads, "!pr/authors"] } }\` (\`references/explain.md\`). The key is the name with no parentheses, and holds for every run of that name. A numbered version has a key of its own, \`repo/change_risk@2\`. Every such list makes merging easier where \`.severity\` is read. A list on \`"**"\` reaches \`.claude/\` and the protected files too. **Lead your reply** with both points:
- Files outside the four paths of the guard ("The review rules themselves"), such as \`CODEOWNERS\` and \`.github/\`, are open to the list, protected or not.
- \`.severity\` is one value for the whole pull request, so a finding resolved on another file still lowers it for them.

**A \`pr/\` or \`rule/\` fact in a rule that reads a classifier with \`findings\`** gives power to whoever can change that fact: it can switch off the run and its open findings, ask for less by itself, or switch who may resolve. Before you put one there, or add a \`findings\` list beside one, read \`references/explain.md\` and follow its part on a fact beside a classifier's findings.

### Labels, reviewers and code

- **\`labels\`:** the run can set labels on the pull request, and swap or remove those it set itself, none whose name starts with \`approvals:\` or \`claude-\`. It creates none: a label that the repository lacks does not come, and the run cannot see which exist, so name each label in the prompt. No rule can read a label. Unless a condition reads the classifier's result, list it under \`advisory\` of an enforced rule. **Warn the person:** an author's text can talk a run into setting any existing label, so do not grant \`labels\` where a label gates a merge or starts a deploy or a workflow.
- **\`reviewers\`:** advanced. A review that must happen belongs in \`seats\`, not in a prompt ("Write one, step by step", step 1).
  - The run adds reviewers on top of what the policy asks: a login, a team of the repository's organization (\`org/team\`) or a \`bot:name\`, but not the latest commit's author. Say in the prompt whom to add.
  - They must approve only where a rule's condition reads the classifier, so give it an output to read. Under \`advisory\` alone they need not. Read in a condition, it can turn pull requests under a directory's own policy file red ("Monorepos, names and versions").
  - For an added reviewer, the approval of the opener, or of the latest commit's author, committer or pusher, does not count. Nor does an earlier approval that only \`reuse\` keeps. On a pull request from a fork, or on a branch with a very long history of pushes, an added reviewer's approval may never count: the classifier must then remove them, so do not promise that their approval turns the check green.
  - No override and no \`seats: 0\` lifts an added reviewer. They stay until the classifier removes them, its first complete run after \`@claude approvals rerun\` or the Re-run button leaves them out, or no rule reaches it.
  - **Warn the person:** a misled run can hold a merge by adding a reviewer who never approves, even one who cannot approve in this repository.
  - While such a run is going or about to start, the check cannot turn green.
  - Do not give \`reviewers\` and \`findings\` to one classifier: most places where a rule could read the pair are refused or blocked. Beside \`findings\` or \`labels\`, a definition with \`reviewers\` takes no \`inputs\` and no version number, and stands under \`advisory\` only in a rule with no \`if\`. No policy file's conditions may read a \`reviewers\` classifier and another with \`labels\`.
- **\`code\`:** the run can also read files beyond the diff: read-only copies of the pull request's head (\`head/\`) and of the default branch (\`default/\`, whatever the pull request's base), without \`CLAUDE.md\`, \`AGENTS.md\`, \`.claude\`, PDFs and a few others. A very large repository gets part of each, picked by what the pull request changes, and the run can ask for more.
  - Grant it only where the question needs more than the diff. Listing it can download those files as the run starts, read or not. A run that reads them waits for them, out of its \`time\`, and pays for what it reads.
  - \`head/\` is the author's version, and \`default/\` is only as well reviewed as the policy makes it ("Recommendations", point 5).

### Built-in limits

A tool call past its limit is refused, and the run goes on. The first four rows count for each version of a classifier on one pull request, and separately for each run that an input with no \`merge\` keeps apart.

| What | Limit |
|---|---|
| Labels it has set | 8 |
| Reviewers it has added | 8 |
| Open findings with a review thread | 16. Any past that is recorded and counts, but gets no thread |
| Repeat runs on one patchset: a rerun and its retries, an identical push, a reopening, being reached again | 10, then one more for each rerun |
| Characters in a finding's text | 2,000 |
| Characters in the comment | 5,000 |
| Other files of its folder that one run reads | 20 |
| Versions in a folder | 8 |

## The prompt

Leave out what Claude Approvals adds itself: the result format and allowed words, and its standing instructions on reading the diff. It also puts a short block before the prompt on every run: what started the run, the open findings' IDs, the inputs' current values, and the rules that asked for the run, with their \`purpose\` and \`paths\`.

Write:

- what each word of \`values\` means and which to pick in doubt. When you trim a prompt, these lines stay;
- what each input value changes. The run is told only the value, such as \`rigor: thorough\`, and an input's \`description\` is not sent;
- what to do with each thing that \`tools\` grants, in plain words and with no tool's name ("Tools and findings"): what to report and at which severity, when to resolve, what the comment holds. "Recommendations", below, says what a good prompt adds.

There are no placeholders: \`{{diff}}\` is sent as typed. The prompt can name another text file of the classifier's folder by its path from that folder, such as \`examples/good.md\`, and the run can read it. Long reference text belongs there. The run reads nothing under \`eval/\`, the place for test cases.

## Recommendations

Good practice for any classifier, beyond what the format demands. Follow it in a new classifier, unless the person wants otherwise. In one that exists, mention what it lacks.

1. **With \`findings\`, write both halves into the prompt: how to find and report a finding, and what to do with the earlier ones.**
   - *Report:* say what earns a finding: a problem that this change brings in, which the run can show from code that it has read. Say what each severity means by its consequence, so that the level a condition tests means what the rule wants.
   - *Earlier findings:* have the run read them first. Still true: it stays open, and is not reported again, in the same words or in others, unless its severity has changed: then under the same title. Fixed by a later push: the run resolves it, and says why (after a person's rerun, it also resolves a finding that it would not report today). Resolved by a person: it stays resolved, and the run re-opens it only if a later push brings the problem back. Not noticing a finding again is no fix, and closes nothing: a fixed finding that the run does not resolve stays open, and can hold the check.
2. **Give a fixed recipe for a finding's title,** such as the kind of problem, with one finding per file and kind, whose text names its other places. The same title on the same file is the same finding, so free wording can open a duplicate at each push.
3. **Define only outputs that a rule reads or will read, say which result to pick in doubt, and have rules name the good result** (\`= pass\`, \`<= medium\`). Never rule out the bad one with \`!=\`: \`!= fail\` is also true of every other word in \`values\`. Add no output that counts or repeats the findings: rules read the worst open one as \`.severity\`, and every output is one more that a run can leave unanswered, which gives no result.
4. **Leave \`budget\` out until you have watched real runs.** A lower \`cost\` saves nothing on a normal run. A run that it cuts off is still paid for and reads \`incomplete\`, and large pull requests meet it first ("No result", "Cheaper and faster").
5. **Judge by what the author cannot change.** What the classifier judges by belongs in its own folder, which is protected. But with no policy file above that folder, as at the root where only directories have one, a pull request that changes nothing under a policy file asks nobody. \`default/\` is only as safe as the policy's review of it, and \`head/\` never is. Have the run go by what the code does, not by what the pull request's title, description or comments say of it.
6. **Ask for sub-agents, which takes a line in the prompt, only where several independent readings are worth the price.** Each reads again, out of the run's own \`time\` and \`cost\`, and only the run itself reports and answers.

## How a rule reads it

Write a read like this, with bare words: \`repo/change_risk@2(rigor=thorough).risk <= medium\`. The version comes first, then the call's inputs, then the output, which is that run's own.

| Form | Example | Reads |
|---|---|---|
| the name alone | \`"repo/change_risk <= medium"\` | the only output, at every \`default\` |
| an output | \`"repo/release_check.kind = docs"\` | one output by name |
| \`.severity\` | \`"repo/change_risk.severity >= high"\` | the worst open finding; needs \`findings\` in \`tools\` |
| a call | \`"repo/change_risk(rigor=thorough) = low"\` | the run with that input |
| \`= error\`, \`= incomplete\` | \`"repo/change_risk = error"\` | how a run ended with no result; \`=\` alone, and never in a \`reuse\` condition |

- A comparison that can never be met is refused.
- Under \`advisory\`, write the name or call with no output.
- As a key of \`reuse\`, write the bare name with no parentheses: it holds for every run of that name (\`references/tune.md\`).
- The built-ins are read the same way (\`references/explain.md\`). The \`level\` of \`claude/code_review\` is an input of \`quick\`, \`standard\`, \`deep\` under \`merge: right\`. Unlike other inputs, it goes by \`paths\` alone, whatever the \`if\`s say. \`claude/diff\` takes no input, and only \`reuse\` reads it.
- A policy file can name at most 16 repository classifiers. Past 8 runs on one pull request, \`reuse\` keeps no more results (\`references/tune.md\`).

A rule **reads** a classifier when its \`if\`, an override's \`if\` or a \`reuse\` condition names it. The check then waits for it, with few exceptions, and it runs when its turn comes, if it does.

## When it runs

- **A run starts when a new patchset starts:** the pull request is opened or aimed at another base branch, or a push changes its diff. So not at every push, and not only at a push. The push must come from an account with write access.
- None starts on a draft: marking it ready starts the run that the draft held back. A label added, edited or removed reruns nothing. In a rule, classifiers start in turn or together, as the policy's \`run\` key says (\`references/tune.md\`).
- **A run completes** when it has read the whole diff, whatever its question, and answered every output, inside its budget. One that does not complete gives no result. Nor does one that Claude Approvals cannot trust, though it answered.
- **The newest completed run's result stands.** It ends at a new patchset, unless \`reuse\` or a push to other rules' files alone keeps it (\`references/tune.md\`), at a rerun, at a changed definition, prompt or input, and at the policy's \`max_age\`. A kept result stands for the whole pull request, the code pushed since included. Where a rule reads it, a reopening can end it too, and the classifier then runs again. On the same commit, merge base and definition, a classifier with no \`findings\`, \`labels\` or \`reviewers\` mostly keeps its result, where no policy file writes \`max_age\`.
- **A person's \`@claude approvals rerun\`, or the Re-run button, is a blank slate.** Every result is dropped, and what the matching rules read or name under \`advisory\` runs again, billed. Where Claude Approvals has only observed the pull request so far, nothing is dropped: a \`repo/\` classifier runs again only if it has no result.
- **Say so where \`code\` is granted:** a merge of the default branch into the pull request can change code that the run read outside the diff. Its result stands all the same.

## No result

Unless an earlier result stands, a classifier with no result reads one of two words, which an \`if\` can compare:

- \`= incomplete\`: the run began and ended by itself with no result. Its budget, time or turns were spent; the diff, the repository (\`code\`) or the conversation was too large to read; or an output was left out or off its scale.
- \`= error\`: most other cases. This includes a run refused before it starts or broken off, and a refused definition. No run starts, for example, where the Claude organization requires self-hosted compute.
- Neither: a run whose answer Claude Approvals dropped or put off, a \`reviewers\` run that stored nothing, or a classifier past its limit of runs. No override catches these. Past the limit of runs, a rule whose reading comes to the classifier holds the check red however many people approve, until a person's rerun or a push that changes the diff starts a run.
- **No usage credits:** where the balance or monthly spend limit of the Claude organization's usage credits has run out, the run gives no result, mostly read as \`error\`, and no edit mends that: an owner of that organization can add usage credits or raise the limit at claude.ai/admin-settings/usage.

What then happens is "How a policy decides", point 3. The red under a rule's own \`if\` also meets the pull request that mends the classifier, where the rule's \`paths\` match the classifier's folder.

**An override on \`= error\` or \`= incomplete\` must not ask for less than the rule's own verdict.** A run with too much to read can end \`incomplete\`, so a missing answer is no sign of a safe change. (For Code Review under a rule that blocks, \`SKILL.md\` has such an override as the way out where no review can start, with its warnings.)

Where a rule reads Code Review below the classifier, where Claude Approvals dropped or put off the run's answer, or where Code Review declines a commit once any \`if\` reads a classifier ("Write one, step by step", step 7), the check can instead say "has not run" or end blocked (\`references/tune.md\`). A missing folder is an unknown name and refuses the policy file.

## Cheaper and faster

1. Let only the rule that needs it read it, on narrow paths. To keep a result after a push, give it a line under \`reuse\` (\`references/tune.md\`). Every other file still needs a rule with no \`if\`.
2. A \`merge\` on every input.
3. A smaller model, such as \`sonnet\` or \`haiku\`. Fast mode (\`-fast\`) is quicker, and costs more.
4. A shorter prompt, fewer outputs, no \`code\` unless needed.
5. \`budget\` caps only the worst case, and spend can pass \`cost\`: say so. A \`cost\` under 5 draws a warning. A run that \`budget\` cuts off reads \`incomplete\`: check that no override asks for less on that.

Each can change who must approve: items 2 to 5 through the results, item 1 as \`references/tune.md\` says. So make one only where the user asked for that very change. Otherwise propose it, name that price, and wait for a yes.

## Monorepos, names and versions

- A policy file finds \`repo/<name>\` in its own directory's \`.claude/classifiers/\` and above, never below. Exactly one of those folders may hold the name: a second one refuses the policy file, so do not reuse a name from above. Sibling directories may use the same name.
- On a pull request under a directory with its own policy file, the check can be red ("Cannot evaluate: classifier outside advisory") where that file, or one above it, reads in any rule, whatever its \`paths\`, a classifier that has the \`reviewers\` or \`labels\` tool, or an input under \`unset\` (no \`merge\`, or \`merge: unset\`). Only under an enforced rule's \`advisory\`, or as a key of \`findings.resolution\`, is such a classifier sure not to cause this. So before you add a directory's policy file, read the files above it for such names.
- The file's name alone says which version it is. \`def.yml\` is the base version, which the bare name means. \`def.v2.yml\` is \`repo/<name>@2\`: a whole definition, with \`prompt.v2.md\` or its own \`prompt\`, which runs only where named.

## Changing a live classifier

- The default branch's copy runs, so a pull request cannot change its own classifier. The folder is protected.
- Any changed byte in \`def.yml\` or \`prompt.md\`, a comment too, ends the stored results. A change to another file of the folder ends none: where it should, change \`def.yml\` or \`prompt.md\` too. The merge itself judges no open pull request again: each check stands, green or red, until that pull request is next judged, and then the classifier runs again. Say that this costs one run for each run that its calls make: calls that a \`merge\` joins share one. So batch your edits.
- Before deleting a folder, remove its name from every policy file in the same pull request.

## A fuller classifier

This one has tools and an input, and keeps its prompt in \`prompt.md\`. A sample's first line only names its file: leave it out of \`prompt.md\`.

\`\`\`yaml
# .claude/classifiers/change_risk/def.yml: the fuller form
version: 1
description: "How risky is this change to ship?"
model: opus
tools: [findings, comment, code]
inputs:
  rigor: { values: [quick, thorough], merge: right, default: quick }
outputs:
  risk: { type: ordinal, values: [low, medium, high] }
\`\`\`

\`\`\`yaml
# .claude/classifiers/change_risk/prompt.md
Rate how risky this change is to ship.
- low: cannot change behavior in production (docs, comments, tests).
- medium: changes behavior in one place that is easy to roll back, or behind a flag.
- high: touches money movement, authentication, a data migration or a shared library, or cannot be rolled back.

When rigor is quick, rate the diff as it reads. When it is thorough, first name every behavior that the diff changes,
error paths and defaults included, and read the callers of each changed function under head/. Then rate the riskiest.
When two levels fit, pick the higher.

Before you report, read the findings that earlier runs of this classifier left on the pull request.
- Still true: leave it open. Report it again, under the same title, only if its severity has changed.
- Fixed by a later push: resolve it, with one sentence on why.
- Resolved by a person: leave it resolved, and re-open it only if a later push brings the problem back.
Then report each new reason for a high rating as a finding, at severity high, on the line it is about, if there is one. Title it by its kind
(money movement, authentication, data migration, shared library, no rollback), with one finding per file and kind, whose text names its other lines.
Keep one summary comment: the rating, and one line per open finding.
\`\`\`

A policy file keeps the long call short in a local, \`locals: { risk: "repo/change_risk(rigor=thorough)" }\`, and reads it in the first rule's override: \`{ if: "claude/code_review = pass AND @risk = low AND @risk.severity <= low", verdict: { claude: approves, seats: 1 } }\`.
