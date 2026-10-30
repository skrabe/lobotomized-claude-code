<!--
name: 'Tool Result: worktree guard computed find paths at once'
description: 'Worktree guard reason that find substitutes all found paths at once with {} +'
ccVersion: 2.1.314
-->
that find replaces with all the found paths at once when the clause ends in `{} +` (do not put `{}` right after an option that takes a value, or end the clause with `\;` so that each run gets one path)
