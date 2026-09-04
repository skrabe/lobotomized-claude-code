<!--
name: 'Data: Review upload excluded changes error'
description: >-
  Error shown when a review upload has no new commits or uploadable changes
  because every uncommitted file was excluded from the git bundle
ccVersion: 2.1.261
variables:
  - GIT_BUNDLE_OPTIONS
  - PLURALIZE_FN
-->
It doesn't look like you have any new commits or changes to review: the only uncommitted changes here are to ${GIT_BUNDLE_OPTIONS.leftOutCount} ${PLURALIZE_FN(GIT_BUNDLE_OPTIONS.leftOutCount,"file")} that ${PLURALIZE_FN(GIT_BUNDLE_OPTIONS.leftOutCount,"stays","stay")} on this machine (named like credentials or keys, ${GIT_BUNDLE_OPTIONS.withheldByRules?"covered by a Read rule or a sandbox read-deny setting of yours, ":""}hard-linked to another file, kept by a git filter such as LFS, or still being written while read) and ${PLURALIZE_FN(GIT_BUNDLE_OPTIONS.leftOutCount,"is","are")} not uploaded. Stage or commit any other work first.
