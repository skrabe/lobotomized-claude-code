<!--
name: 'Tool Result: Steward push refs unlistable'
description: Refuses a push when git cannot list or trust the checkout's refs
ccVersion: 2.1.330
-->
git couldn't list this checkout's refs, or one of them is broken or out of place, so the commit that a push would send can't be told. Push nothing, and tell the user, who can run git show-ref to see which
