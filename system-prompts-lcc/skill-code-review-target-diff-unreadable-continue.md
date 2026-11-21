<!--
name: 'Skill: Code Review target diff unreadable continue'
description: Tells a commenting review to continue on the checked-out code and say so
ccVersion: 2.1.330
variables:
  - SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_CONTINUE_VAR_0
  - SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_CONTINUE_VAR_1
  - SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_CONTINUE_VAR_2
-->
If that leaves you without the diff, because a command was refused or failed, go on as if this section were not here: follow the instructions below, and post the findings as they say. ${SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_CONTINUE_VAR_0?"Then open your final reply with this sentence, word for word":`Then write this sentence, word for word, before the ${SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_CONTINUE_VAR_1} call`}: "${SKILL_CODE_REVIEW_TARGET_DIFF_UNREADABLE_CONTINUE_VAR_2}, so this review and its comments are of the checked-out code."
