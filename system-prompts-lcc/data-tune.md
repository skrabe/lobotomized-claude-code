<!--
name: 'Data: tune'
description: >-
  claude-approvals skill reference file for simplifying and tuning a policy
  file.
ccVersion: 2.1.332
-->
# Claude Approvals: simplify and tune a policy file

A reference file of the skill \`claude-approvals\`. Read \`SKILL.md\` first: everything there above "Workflow" binds here too. A section named in quotation marks that this file lacks stands there. \`SKILL.md\` and \`references/...\` count from the skill's folder, not from the repository.

**Contents:** Simplify: procedure; Safe rewrites; Merging twin rules; Look safe, and are not; Show that it decides the same; Example: sharing through locals and use; Cost and speed: what costs what; What runs when; run: sequential or parallel; The levers, best first; reuse for cost; Review a policy.

## Simplify: procedure

The goal is a file that is easier to read and decides **exactly** what it decided before. Work from the lists below, not from judgment.

1. **Read every policy file and classifier folder.** Locals and \`nested: inherit\` rules reach the files below. A file without \`version: 1\` is not covered by this skill: say so, and change nothing in it unasked.
2. **Collect candidates,** most repeated first. Anything in no list below belongs with "Look safe, and are not".
3. **Apply the safe rewrites,** one kind at a time, all through the file. Then merge twin rules where every condition holds. A clean-up that leaves the repetition is not done.
4. **Show sameness.** If you cannot show it for a rewrite, take it back.
5. **Report:** whether, as far as you could check, the new file decides every pull request as the old one did, and whether that rests on a check you ran or on reasoning alone; size before and after; which classifiers will run again on open pull requests; each thing the user suggested and you did not do, and what it would have changed. List apart what looks like a **bug in the policy** (a rule with no effect, a pattern that matches nothing), as a question: fixing it changes decisions.

## Safe rewrites

- \`seats: [{ count: 2, from: humans }]\` to \`seats: 2\`; \`seats: []\` to \`seats: 0\`; \`from: [humans]\` to \`from: humans\`; \`[humans, bots]\` to \`everyone\`. In an override, keep the set (\`{ count, from }\`) where the rule's own \`seats\` names people or teams or has a \`"!"\` item: a bare number there draws a warning.
- Delete a written default (\`mode: enforce\`, \`nested: overwrite\`, \`run: sequential\`; on a rule \`if: true\`, \`override: []\`, \`advisory: []\`) only on a rule with no \`use\`, and only where the top of the file writes no other value for that key. Under \`use\`, an \`if\`, \`override\` or \`advisory\` written in place replaces the used local's: deleting it brings the local's back.
- Move \`run\`, \`nested\` or \`mode: observe\` once to the top only where **every** rule has it and none writes another value. A rule without it would change too: with \`run: parallel\`, for example, it would start and pay for all its classifiers at once.
- Delete an override that can never be chosen: its condition is that of an override **above it in the same rule**, alone or with more joined by \`AND\` (\`"claude/code_review = pass AND pr/diff_lines <= 20"\` below \`"claude/code_review = pass"\`). Only where it asks no more than that one and the rule's own verdict, has no \`reuse\` or \`findings\` (written or through \`use\`), names each classifier with the same inputs or \`level\`, and is not the only place naming a classifier or \`level\`. A "cannot tell" warning is then expected: say so.
- In an override, delete a field that repeats the rule's own, keeping at least one of \`verdict\`, \`reuse\`, \`findings\`. Never delete the override; leave \`findings\` alone. In a local: only if every rule using it says the same.
- Flow to block style or back; parentheses around a single comparison removed; quotes added, never removed.
- A repeated list, set, or shared \`verdict\` and \`override\` moved into \`locals\` and brought in as \`"@name"\` or \`use: ["@name"]\`. The name must be new in this file and in the files above and below. A map takes \`verdict\`, \`override\`, \`if\`, \`paths\`, \`reuse\`, \`advisory\`, \`findings\`; not \`purpose\`, \`mode\`, \`nested\` or \`run\`.
- A local used once written out in place; an unused local deleted. Only where no policy file below names it: that file would be refused.
- Comments changed or deleted; commented-out rules deleted.
- A pattern or login twice in one list, once deleted. Not on a rule that names a \`repo/\` classifier.

## Merging twin rules

Rules of one file that differ **only** in \`paths\` and \`purpose\` can become one. Compare them after the safe rewrites: \`from: [x]\` and \`from: x\` are the same, and so are the same sets in another order. Merge only where **all** hold:

1. No twin reads a count (\`pr/files_...\`, \`rule/files_...\`), has a \`reuse\` key, or a \`"!"\` item in its \`paths\`.
2. No **other** rule that can apply to the same pull requests reads \`pr/files_changed\` or \`rule/files_changed\`, except exactly \`"rule/files_changed = pr/files_changed"\`: a file moved between twins counts as two files before and one after.
3. They agree in \`mode\`, \`nested\`, \`run\`, \`if\`, \`verdict\`, \`override\`, \`advisory\` and \`findings\`, and name no \`repo/\` classifier.

If one fails, do not merge: share the verdict and overrides through \`locals\` and \`use\` (see the example), and say which condition failed.

**A cost to name.** A \`repo/\` classifier is asked with the rules that name it and match the pull request: their order, \`purpose\` and \`paths\`. A new order or \`purpose\` among those rules ends its stored results on that pull request: it runs again, billed, when next judged, and may give another result. Changing only \`paths\` mostly makes it run, perhaps for the first time, where that moves one of the pull request's changed files onto or off a rule naming it. It can also run again elsewhere, as on an older stored result or one that \`reuse\` kept, so promise no saving. Say the cost, and that a result may change.

## Look safe, and are not

Besides "Edits that look stricter or harmless":

- Deleting a \`"!path"\` item because another rule handles that path: the broad rule now holds there too.
- Deleting a rule whose \`if\` is never true: a file only it covers goes from a red check to nobody asked to review it.
- \`[{ count: 1, from: a }, { count: 1, from: b }]\` to \`[{ count: 2, from: [a, b] }]\`: two people from team a alone now pass.
- \`reuse: { seats: C }\` to \`reuse: C\`: the short form can also keep every classifier result the rule reads. Deleting a rule's \`reuse\` because another rule has one, or the reverse: each rule has its own say.
- Adding, widening, moving or deleting a \`findings\` list (who may close a finding by resolving its thread):
  - Where a condition asks for less on \`.severity\` (the worst open finding) or on Code Review's \`= pass\`, or a stricter verdict hangs on its \`= fail\`, whoever a list lets in can resolve threads and get that at once, nothing fixed and no new review (the answer turns only where the lists let them in on every changed file under a rule that compares it, so taking \`nobody\` off a sensitive path also frees the pull requests that change it beside other files). On Code Review's own threads \`bots\`, \`everyone\` and \`bot:claude\` let in every Claude session that resolves under Claude's Apps: say so, and offer \`"!bot:claude"\` beside them (for \`everyone\`, \`[humans, bots, "!bot:claude"]\`).
  - Each list only narrows the others: deleting one beside another lets more accounts in.
  - **Code Review's list, where a condition in any policy file compares its answer** (\`= pass\`, \`= fail\`, \`!=\`), whether or not another reads its \`.severity\`: with no list of its on a file, no new resolve by a person there lowers \`.severity\`, and where an enforced rule reads \`claude/code_review\`, none turns its \`fail\` into \`pass\`. Count on that only where an enforced rule with a \`verdict\` and a condition on its \`= pass\`, \`= fail\`, \`!=\` or \`.severity\`, a \`reuse\` line's too (holding its list is not reading it), matches the file, has no \`if\` of its own and stands in the policy file that would decide there if every rule's \`if\` held; else promise nothing. So an edit that leaves a file with no list of its, by deleting a list or moving it to other \`paths\`, **gets the guard, whichever case holds**: for Code Review it changes nothing where no resolve counts, and it keeps the review rules shut where a resolve can count. So does an edit that takes a narrow list off a file that a wider list still reaches: it lets in whoever only the narrow list kept out. Of "The review rules themselves" only "First:" and the guard apply: add no copy, and where another list reaches those paths, another classifier's or Code Review's own, name who loses it. Where the file is left with no list, look for that rule. Found: name it, with its condition, skip "say whom it shuts out", and say that the edit lets nobody new resolve there, that whoever the list named loses this by the edit, not by the guard, and that a finding there, or, where that condition compares the answer, anywhere in a pull request that changes the file, can then hold the stricter verdict. Not found, or in doubt: say that deleting a list is no way to shut people out there, treat the edit as one that can make merging easier, and offer \`nobody\` on a rule with no \`if\` of its own.
  - **A \`repo/\` classifier's list, and Code Review's where no condition in any policy file, a \`reuse\` line's too, compares its answer:** with no list no person's resolve counts toward \`.severity\`. So deleting the only such list that reaches a file, or moving it off that file, lets nobody new in there: say that whoever it named loses this, and, where a condition reads its \`.severity\`, that a finding can then hold a pull request red.
  - On \`"**"\` it reaches the protected files: add the guard that "The review rules themselves" asks for, where it asks for one; add it beside the copy too, even where the old rule had a list. **Lead your reply** with what stays open (\`.github/\`, \`CODEOWNERS\`) and that \`.severity\` is one value for the whole pull request. A list the person gives as YAML, \`humans\` too, goes in unchanged: add it, and say whether it takes in the author.
  - Where a condition compares Code Review's answer (\`= pass\`, \`= fail\`, \`!=\`) and none reads its \`.severity\`, a new list of Code Review's, or one whose \`paths\` change, other than \`nobody\`, needs the guard and no copy if its \`paths\` can reach a file on the guard's four paths that no list of its on an enforced rule in that policy file reaches yet (\`"**"\` above all; \`src/**\` can reach \`src/REVIEW.md\`), and so does an edit that lets anybody new resolve on such a file that a list of Code Review's reached before the edit. Where no condition reads either, a list written under Code Review's name needs no guard, until an edit adds the first condition on its answer. Follow "Who may dismiss a finding" in \`SKILL.md\` for what to write and what to tell the person, in place of the lead above.
- \`dir/**\` for \`dir/**/*\`, \`**/*.md\` for \`*.md\`, two patterns for a \`{a,b}\` group: they match different files, or the check cannot tell.
- Moving a rule between the root's file and a directory's, or a first rule in a directory's file: that file may now decide, and a \`repo/\` classifier named there or above can turn every pull request under it red (\`SKILL.md\`, on a directory's own policy file). Deleting \`nested: inherit\` "because no file lies below": the next directory file escapes it.
- Deleting \`advisory: [claude/code_review]\`: Code Review may stop starting by itself. Moving a classifier between \`advisory\` and an \`if\`: it now decides, or no longer does.
- \`mode: observe\` on some rules turned into the file's \`mode\`, or back; renaming a local (a file below may read the old name), or adding one whose name a local below already has.
- \`run\` changes or facts added "while we are here": that is tuning; keep it out of a clean-up.

## Show that it decides the same

1. **By construction:** name each kind of rewrite applied.
2. **The product's comparison:** on a pull request into the default branch, Claude Approvals compares the new root file, and each directory file the pull request edits, with the old, and warns where a change may ask for less ("this rule no longer holds on these files", "cannot tell"). A warning means: show sameness another way, or take the rewrite back. On a branch that is behind, update it first and look again. Silence says nothing of a deleted directory file, a borrowed local, or a \`nested: inherit\` rule of a directory's file that stops holding under a policy file the pull request leaves alone.
3. **Cases:** for each touched rule, walk old and new once per verdict it can pick (its own, each override, **no result** from each classifier), with a person and a bot as author, zero, one and two approvals, and a file renamed between merged rules. Say "I found no difference in these cases", not "proven".

## Example: sharing through locals and use

After the safe rewrites (the last rule is unchanged):

\`\`\`yaml
# .claude/approvals.yml: a sample, not the user's file
version: 1
locals:
  payments_owner: { count: 1, from: [acme/payments, acme/payments-leads, "!pr/authors"] }
  payments_review:  # two people, one of them a payments owner; on a pass of a small change the owner alone
    verdict: { claude: comments, seats: [{ count: 2, from: humans }, "@payments_owner"] }
    override:
      - { if: "claude/code_review = pass AND rule/files_changed <= 5", verdict: { seats: ["@payments_owner"] } }
rules:
  - purpose: "The payments API takes two people, one of them a payments owner who is not an author."
    paths: ["services/payments/api/**"]
    use: ["@payments_review"]
  - purpose: "Everything takes two people. One when Claude's review passes."
    paths: ["**"]
    verdict: { claude: comments, seats: 2 }
    override:
      - { if: "claude/code_review = pass", verdict: { claude: approves, seats: 1 } }
  - purpose: "Payments jobs take two people, one of them a payments owner who is not an author."
    paths: ["services/payments/jobs/**"]
    use: ["@payments_review"]
  - purpose: "A change to the review rules takes two people."
    paths: ["**/.claude/**", "**/REVIEW.md", "**/.gitattributes", "**/.gitmodules"]
    nested: inherit
    verdict: { claude: comments, seats: 2 }
\`\`\`

The two payments rules are **not** merged: their override reads \`rule/files_changed\`, which would then count both folders' files. The \`"**"\` rule was left as found: it has the starter's override, and changing its \`seats: 1\` would be no clean-up ("Review a policy").

## Cost and speed: what costs what

- **Money:** every classifier run (Code Review, \`repo/\`, \`claude/diff\`). Rules, facts and approvals are free.
- **Time:** the check waits for the runs the rules read, down to the first true override, not for what only \`advisory\` names.
- **Both mostly repeat at every push that changes the diff,** unless \`reuse\` keeps the result (Code Review: see "What runs when").
- **\`mode: observe\`:** classifiers still run and are billed, and \`reuse\` skips nothing, except that, where only Claude Approvals' request brings the review, a \`claude/code_review\` line can keep an earlier pass, and no review is asked for. Do not count on \`sequential\` to save runs there.

Make the changes that cut what the user named and keep who must approve, and give each its change in runs. Propose, with its price, any that lets more merge unasked (a \`seats\` line under \`reuse\`, say). Count runs per kind of recent merged pull request, before and after. Give no prices or durations you have not measured.

## What runs when

- A classifier runs only where a matching rule names it (Code Review can still start by its own setting on some pull requests, such as ones under no policy file). In an \`if\`, an override's \`if\` or a \`reuse\` condition it is waited for when its turn comes (see \`run\`), until the check's wait ends. Named only under \`advisory\`, it mostly runs again at a push that changes the diff (Code Review: where it reviews every push) and is never waited for.
- Several classifiers in **one** condition start together, whatever \`run\` says.
- Nothing runs on a push from an account without write access, until a person with write access comments \`@claude approvals rerun\`: a check that needs a run to pass is red meanwhile.
- A false fact in an override's \`if\` saves nothing; a false fact in the rule's own \`if\` stops its \`repo/\` runs, not \`advisory\`.
- **Where Code Review reviews only on request, or is off for the repository or for the organization,** Claude Approvals asks for each review itself, billed: at each opening, reopening, marking ready, push and change of base, where an enforced rule's reading comes to a condition on it (a \`reuse\` condition alone asks nothing) and no earlier result still counts, unless the check is already green without it.
  - **Green from the start.** It can be from the start, where only overrides read the review and every verdict the rules can pick is \`seats: 0\`, or a \`seats: 1\` that the author fills: no review is then asked for, and a rule's own \`comments\` stops Claude approving until one has passed. Say so before you write such a rule, and that a person with write access can ask for the review, billed, with \`@claude review\` alone on a new comment's first line, though that can be refused where Code Review is off for the organization.
  - **After \`mode: observe\` goes.** On the terms above, Claude Approvals also asks at the first evaluation that enforces after a file-wide \`mode: observe\` goes, with no push.
  - **After an error.** On github.com it can ask again by itself, for about two hours, after a review that ended in an error: unless the check goes green first, it stays in progress meanwhile, and what the file asks on an error holds only after that.
  - **To stop it.** Switching Code Review off stops none of it, the compliance case below aside: to stop it, take \`claude/code_review\` out of the conditions. Turning Claude Approvals off for the repository, in the admin settings, stops it too, but ends every rule there: a check that the branch requires then cannot pass, and elsewhere none of its rules holds a merge back.
  - **Claude Approvals asks for none:**
    - on a draft or a fork;
    - for an organization barred from classifier sessions;
    - in some organizations that never set Code Review up (the review reads \`error\` at once, so an override that blocks on \`= fail\` never blocks there; the check may still say that Code Review is off for the organization);
    - in an organization whose compliance settings keep Claude Approvals from starting Code Review (the same, as a rule);
    - where another Claude organization has the repository in its Code Review;
    - in a few other set-ups (mostly \`error\` at once too, so until a review has landed, do not count on an override that blocks on \`= fail\`).
- **The spending limit on the reviews that Claude Approvals asks for.** Where such an ask is what first sets up Code Review's billing, that can come with a monthly spending limit; billing that already exists keeps its limit, or its lack of one. Once that billing exists, an Owner of the Claude organization can see and change the limit at claude.ai/admin-settings/usage, on the Claude Code Review row under Services. Once it is spent, paid reviews mostly stop and \`claude/code_review\` mostly reads \`error\`.
- **Under a file that only observes,** Claude Approvals asks as if the file enforced, for the reviews that Code Review's own setting does not start, billed, so it can cost reviews that did not run before.
- **A later push**, where Code Review reviews once when a pull request opens: Claude Approvals may ask for a billed review itself, unless an earlier result still counts or the check is already green without it, and on github.com can ask again after a review that ended in an error (above). If none comes, the review can count as \`error\`, so a file that asks less on \`= error\`, or in the rule's own verdict, can go green with no review.
- **A resolve of one of Code Review's threads** starts no review, with or without a \`findings\` list: not a click on Resolve, not \`@claude approvals resolve\`, not a reply in a thread. A listed account's resolve counts at once instead (\`references/explain.md\`, "After a failed Code Review: when a resolve counts"). Where resolves turn a failed review into \`= pass\`, a \`repo/\` classifier held back behind that condition can get its first run, billed.
- **A \`repo/\` classifier in an override above Code Review has no result while the review is held back for its turn:** mostly nothing asks for the review, and at the wait's end the check can end blocked, whatever the file says on \`= error\`. Approvals enough for the rule's own verdict and every override that could still be picked turn it green; \`@claude approvals rerun\` runs the classifier again and asks for the review at once.
- **"\`repo/x\` has not run", "reached its run limit", "A classifier's result no longer counts":** that classifier's result does not count. The check is red whoever approves, under an override too: a \`repo/\` classifier that has not run holds it until a run gives a result. A new Code Review does not help; where the classifier stands in an override above Code Review, this red comes only after a review has landed. \`@claude approvals rerun\` can start it again, billed (past the limit of 10 repeat runs on one diff, one more run each time; at the 24-hour limit of automatic re-runs, it can set off more automatic runs, billed too; nothing on a draft; on a fork only a typed command by a person with write access, not the Re-run button); do not suggest it while a run is going.

## run: sequential or parallel

\`run\` stands at the top or on a rule; the rule's wins. It sets whether a rule's \`repo/\` classifiers take turns. **It never changes which override is chosen for the same results.** Where a classifier with the \`reviewers\` tool can add people, it can change who must approve and when the check can turn green; where an override writes a shorter \`max_age\`, it can change when the check turns red: in both, propose, do not make, the change.

| | \`sequential\` (the default) | \`parallel\` |
|---|---|---|
| The next override's \`repo/\` classifiers | once every override above is false | already started |
| Money, roughly | the \`repo/\` runs down to the first true override | every classifier that the rule names |
| Time, roughly | the **sum** of those runs | the **longest** of them, down to the first true override |

- **Choose \`parallel\`** on a rule where most pull requests fall through to the last override anyway: the same money, less time.
- Where a rule's conditions read only one classifier, \`parallel\` gains no time.
- Write \`parallel\` on the one rule that needs it, and name its price where pull requests stop at an earlier override or a false \`if\` of the rule's own: more paid runs at every push, and a run that may add reviewers keeps the check from green while it is going or about to start.
- **Putting a cheap override above an expensive one** changes decisions: do it on the user's word, naming the pull request that now comes out differently.

## The levers, best first

- **\`reuse\` with \`claude/diff\`** on rules naming an expensive classifier: often the largest saving; it changes who must approve, on purpose. Unasked, propose it, with the prices under "reuse for cost".
- **Narrower \`paths\`** on the rule that names the classifier: mostly a free lever for Code Review and \`advisory\`. Files that leave need another enforced rule with a \`verdict\`. This changes who must approve there: propose it.
- **A fact in the rule's own \`if\`** (\`"pr/diff_lines > 20"\`): another enforced rule with a \`verdict\` and no \`if\` must cover where it is false, so who must approve changes there: propose it. For \`tools: [findings]\`, read \`references/classifiers.md\` first and say what it costs: the run and its open findings go too. Never on a rule that compares Code Review's answer or holds a \`findings\` list of Code Review's, even a list of \`nobody\`: both need a rule with no \`if\` of its own. Propose the fact-only override below instead: it leaves who may resolve as it is. It saves a review only where Claude Approvals asks for it: where Code Review reviews every push by its own setting, that review mostly still starts.
- **A fact-only override**, with the rule's own verdict, directly above the one override reading the \`repo/\` classifier it skips. It keeps the same approvals only where all hold: under \`sequential\`; below every override reading another classifier; its fact making every override below false; counts or \`pr/base\` only. A fact on people (\`pr/authors\`, \`pr/opened_by\`) stays joined to its classifier. Otherwise it shields every override below: propose it, with the pull request that comes out differently.
  - Never where the classifier can add reviewers: the people it would have added are no longer asked, and with \`tools: [findings]\` too, matching pull requests are blocked without being evaluated.
  - For \`tools: [findings]\`, say first that whoever can change the fact can switch off the run and its open findings, that a fact at or above the last override reading the classifier never chooses who may resolve them, and that where the rule has an \`if\` of its own, its list alone lets nobody resolve them.
- **Drop \`advisory\` lines nobody reads,** but leave one that calls with other inputs (removing it changes the run the rules read) or is the only key keeping a rule with no \`verdict\` valid. Propose, not make, removing the only mention of \`claude/code_review\`.
- **\`merge\` on a classifier's inputs** (\`references/classifiers.md\`): one run in place of one for each value; every rule then reads the one run at the merged value, deeper or lighter than it asked, so it can change results, and who must approve. Under \`left\` or \`min\` the lightest value asked for wins: prefer \`right\` or \`max\`. Propose it, with that price.
- **A smaller model, shorter prompt, fewer tools, \`budget\`** (\`references/classifiers.md\`): can change results, so who approves. Make them only where asked for that very change; otherwise propose with that price. \`budget\` saves nothing on a normal run; it caps the worst case, and a run it cuts off reads \`incomplete\`.

## reuse for cost

\`\`\`yaml
# in .claude/approvals.yml, on a rule
    reuse:
      seats: "claude/diff <= same_intent"            # people's approvals still count
      claude/code_review: "claude/diff <= trivial"   # can keep the earlier review's result: see below
      repo/change_risk: "claude/diff <= same_intent" # the earlier rating can still count, with no new run: see below
\`\`\`

- Each line can keep one thing while its condition holds. Leave out \`seats\` to keep results but not approvals.
- \`claude/diff\` rates what changed as \`trivial\`, \`same_intent\` or \`different\`, in that order.
  It gives no rating, and nothing is kept on it, where a push leaves the pull request changing a build or CI file that the approved diff did not name: mostly a Gradle or Bazel build file, a script in a folder named \`ci\`, a workflow in the root's \`.github/workflows/\`, or a file under \`.buildkite\`.
  Where a person without confirmed write access opened the pull request, it keeps approvals only over a push that leaves the pull request's own changes as approved; it still rates kept results.
- **For \`claude/code_review\`, propose the line (write it only if asked), and promise no saving:** where Code Review reviews every push, the new review mostly still runs, billed, and the check mostly waits for it: the old pass is mostly kept there only where every changed file lies under a policy file and no rule of any policy file above a changed file, matching or not, reads the review other than as \`claude/code_review = pass\` in an override. Nor is a review mostly kept, under \`true\` too, where an enforced rule that matches a file of the pull request reads its \`.severity\` and it has a thread, open or resolved, on a file of the pull request. Where it is kept, an old pass can count for a push no review read; where only Claude Approvals' request brings the review, none is asked for once approvals turn the check green, and a \`seats\` line can keep such approvals after a push.
- **Every rule counts for itself:** a result is kept only if every rule matching a file changed since the run, and reading or advising that classifier, has a line for it that holds. Write it on the \`"**"\` rule too. The policy files above the one that decides have a say as well, marked \`nested: inherit\` or not: where a root rule on that file reads \`repo/x\` with no line for it, a line in the directory's file alone keeps nothing.
- **A kept result does not last:** from the second push that changes the diff after its run, \`claude/diff\` also compares with what that run read, and after four such pushes at most the classifier runs again. The base branch must have stayed the same. No line keeps a result or an approval over a push that changes a protected file, and a file that has left the pull request since the run ends its result.
- **An open finding can end a kept result sooner.** Under a condition on \`claude/diff\`, a \`repo/\` classifier mostly runs again, billed, within two pushes that change the diff, while it has a finding open and an enforced rule that matches a file of the pull request reads its \`.severity\`; with no such rule it can run again too. Under \`true\` the result can stay kept; under a condition that reads only facts or another classifier it can stay kept or run again, billed. Promise no saving, and no run: a result that stays kept can leave a fixed finding open until a person with write access comments \`@claude approvals rerun\` (billed).
- **A failed Code Review.** Where Code Review reviews the new commit, a failed review is not reused. Where it does not, to have a failed review reviewed again after a small push, give its line a condition on \`claude/diff\`, not \`true\`, and have every enforced rule that matches a file of the pull request read the review only as \`claude/code_review = pass\` in an override, with no other kind of override below it: a new review is then mostly asked for, billed, but promise none. Change a rule for this only if the person asks, and say what a condition that you take out was holding: an override on \`= fail\` or \`.severity\` may be what blocks. Read any other way, a line that holds can go on keeping the fail, and a fix can leave its findings open. Where no new review comes, a person with write access comments \`@claude review\` or \`@claude approvals rerun\` (billed).
- **A \`seats\` line** is tested apart for each approval, against the commit that it was given on. It keeps an approval only if every rule on a file changed since, that could count that person, has one that holds. A rule could count whoever the items without \`!\` in its sets name, and anyone where an item is a fact or a team that could not be read: so a \`"!"\` item keeps a person out of the seats, yet the rule can still drop their approval. In a set whose \`from\` is anything but \`humans\` alone, a kept approval fills a seat only if one of the rule's files was in the diff that the person approved.
- **Name the loosening:** a \`seats\` line keeps past holders of the author's seat (such as the previous latest commit's author, or the opener), so two of them, or one beside the latest commit's author, can fill \`seats: 2\` with nobody approving, and more of them can fill a larger number.
- **GitHub's own rules still apply:** where GitHub requires approvals and "Dismiss stale pull request approvals when new commits are pushed" or "Require approval of the most recent reviewable push" is on, GitHub can still want a new approval after the push, even where the check keeps the old one: say so, and that this is no reason to switch a setting off. Before joining a second classifier to the \`seats\` line by \`AND\`, say that with it the check never keeps a review that GitHub dismissed at the push ("Dismiss stale").
- A classifier read by a \`reuse\` condition must not have a line of its own in that file: the file is refused. Its own earlier result is mostly not reused.
- A numbered version's result (\`repo/<name>@2\`) is kept only by a line under its exact name, or by one condition for all that \`use\` brings, and a line under any version of the name can drop it.
- Of the \`repo/\` runs read by the rules that match a pull request (\`advisory\` aside), only 8 can take over an earlier result after a push, whatever \`reuse\` says, chosen mostly by name, so a new name can push out an older one. The rest mostly run again, billed, the check waits for them, and nothing warns. Let a pull request reach a ninth only where the user asks for it, and say that price.

## Review a policy

For "is this good?" or "make it better", report in this order, then cost, speed and legibility.

**First hold it against the starter** (printed whole in \`SKILL.md\`, where it speaks of a first policy file), which Anthropic's quickstart and docs begin with. Say which of these the file lacks: a rule on \`"**"\` with no \`if\`; the strict verdict on the rule itself, and less only in overrides that read a classifier; a rule on \`"**/.claude/**"\` marked \`nested: inherit\`. The starter's own override, \`approves\` and \`seats: 1\` on \`claude/code_review = pass\`, on the \`"**"\` rule with no \`if\`, beside that rule's own bare \`seats: 2\` or higher, is the recommended start and no finding. Say once what it means: on a pass the author and Claude can be enough, on protected files outside \`.claude/\` too (and, with no rule on \`.claude/\`, there too), and a pass does not mean that every changed file was read. Mention both options, \`seats: 2\` there or a set that leaves authors out, and make neither unasked. Where the file is one of the two other starters in \`SKILL.md\`, the small file or the root file that passes everything, say which, and report what it lacks as that starter's known limit. Count who has write access before proposing a rule that asks two people: with one person it locks.

**1. Changes that could merge with nobody looking:** \`claude: approves\` as a rule's own verdict or in an override that reads no classifier; a rule's own verdict asking nobody (neither is a finding in a rule that asks nothing beside an enforced rule with a \`verdict\` and no \`if\`, in the same file, that matches all its files: \`SKILL.md\` writes \`{ claude: approves, seats: 0 }\` to carry a \`findings\` list, and \`{ claude: comments, seats: 0 }\` to stop Claude approving); \`approves\` beside \`seats: 1\`, or \`claude/code_review = pass\` asking nobody but the author, in any override but that one of the starter's (the author fills the seat, and a pass does not mean that every changed file was read); any other override that asks less than its rule, on a rule that reaches \`.claude/\`, and the starter's own where no stricter rule without such an override also matches \`.claude/\`; overrides asking for less on \`pr/opened_by\`, \`ANY pr/authors\`, \`bots\`, or on \`OR\` between a fact and a classifier; \`= error\` or \`= incomplete\` asking for less (under a rule that blocks until Code Review passes it is the known way out: name its price, and do not propose removing it where no review can start); \`claude/code_review = fail\` alone (join \`claude/code_review.severity >= high\` by \`OR\`; see 2 on \`.severity\`); \`findings\` lists taking in authors or bots; a \`from\` that holds a bot (\`bots\`, \`everyone\`, a \`bot:\` name, \`pr/opened_by\` or \`pr/authors\`, with no \`"!"\` item taking it out), whatever the verdict's \`claude\` says: a bot that opened the pull request and pushed its latest commit fills that seat with nobody reading, and where the list lets Claude in (not a \`bot:\` name other than \`bot:claude\`) beside \`approves\`, Claude's approval can fill it too; \`reuse: true\`, or any \`reuse\` that keeps \`seats\`, above all one not reading \`claude/diff\`; a directory file asking less than the root; files no enforced rule with a \`verdict\` matches.

**2. Pull requests that can get stuck red:** files whose only rules have an \`if\`; a classifier in a rule's own \`if\`; a \`.severity\` condition, or \`blocks\` until \`claude/code_review = pass\`, with no \`findings\` list (a list cures it, for \`= pass\` only where it lets the resolving account in on every changed file under a rule that compares the answer, and makes merging easier: name whom it lets in); \`blocks\` whose only way out reads Code Review, where no review can start or it has no result; a rule that reads Code Review, where any rule that matches a file of the pull request has an \`if\`, its own or an override's, on another classifier, or writes a \`level\`: where Code Review declines the commit, or a rerun dropped its result and no new review comes, the check can stay red ("Code Review has not run") whoever approves; sets that leave authors out and name no more logins than \`count\`.

**3. Lines that seem to do nothing:** an override below one always true; an \`= error\` line below the override reading the result; a narrow rule asking less beside a broad one. List the last as a question, never delete it in a clean-up. Delete the first two only as the safe rewrite on overrides that can never be chosen allows.

For each finding give the line, why it matters, and the proposed edit. Where asked to make it better, apply at once only what changes neither who must approve, who may resolve, nor what is paid; propose the rest (this holds over "Start here", point 2).
