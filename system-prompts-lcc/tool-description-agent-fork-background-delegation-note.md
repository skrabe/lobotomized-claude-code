<!--
name: 'Tool Description: Agent (fork runs in background)'
description: >-
  Agent tool description fragment explaining that a fork runs in the background,
  keeps its tool output out of the parent's context, and that the fork itself
  must execute directly rather than re-delegate.
ccVersion: 2.1.232
-->

A fork runs in the background and keeps its tool output out of your context. If you are the fork, execute directly — don't re-delegate. Subagents notify you on completion; until then, report them as pending rather than predicting their results.
