<!--
name: 'Skill: Code Review CLAUDE.md violation evidence rule'
description: Requires quoting the exact CLAUDE.md rule and line before flagging a violation
ccVersion: 2.1.330
-->
Only flag a violation when you can quote the exact rule and the exact line
that breaks it — no style preferences, no vague "spirit of the doc"
inferences. In the finding, name the CLAUDE.md path and quote the rule so the
report can cite it. If no CLAUDE.md applies, return nothing for this angle.
