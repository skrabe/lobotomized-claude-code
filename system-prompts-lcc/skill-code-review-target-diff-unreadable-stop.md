<!--
name: 'Skill: Code Review target diff unreadable stop'
description: >-
  Tells the review to stop and post nothing when a fix or URL target diff can't
  be read
ccVersion: 2.1.330
variables:
  - SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_STOP_VAR_0
  - SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_STOP_VAR_1
-->
If that leaves you without the diff, because a command was refused or failed, stop: post nothing, change no file, make no ${SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_STOP_VAR_0} call, and reply with only this sentence, word for word, and no list of findings, not even an empty one: "${SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_STOP_VAR_1}, so nothing was reviewed."
