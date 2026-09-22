<!--
name: Code-review launched acknowledgement instruction
description: >-
  Meta-message injected into the model's context after an ultra code review
  launches, instructing it to briefly acknowledge the visible output without
  repeating the target, URL, or billing note.
ccVersion: 2.1.218
variables:
  - SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_0
  - SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_1
  - SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_2
  - SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_3
-->
The output above is already visible to the user. Briefly acknowledge it without repeating the target, URL, or billing note. Findings will arrive via task-notification.${SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_0?" The user passed --fix: when the findings arrive, apply them to the local working tree.":""}${SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_1?` The user's argument was interpreted as a review note, not a base branch: "${SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_2(SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_1,SYSTEM_REMINDER_REVIEW_LAUNCHED_ACKNOWLEDGE_VAR_3)}". The cloud review runs its standard pass over the branch diff and does not see the note; when the findings arrive, prioritize and relate them to the user's request.`:""}
