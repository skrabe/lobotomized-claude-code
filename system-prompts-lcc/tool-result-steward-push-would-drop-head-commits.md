<!--
name: 'Tool Result: Steward push would drop head commits'
description: Steward hook refusal of a push that does not build on the pull request's head
ccVersion: 2.1.331
-->
the pull request's head on GitHub holds commits that this push doesn't build on, so it would drop them. Fetch and merge the head branch first, then push. If this comes again after that merge, push nothing, and tell the user
