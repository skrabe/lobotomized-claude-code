<!--
name: 'System Reminder: Scheduled prompt skill approval pending'
description: >-
  Meta message saying a scheduled prompt has not run because it may need user
  approval, telling the model to call the named tool for each listed skill with
  the prompt's arguments and not to do the skill's work another way if refused.
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_SCHEDULED_PROMPT_SKILL_APPROVAL_PENDING_VAR_0
  - SYSTEM_REMINDER_SCHEDULED_PROMPT_SKILL_APPROVAL_PENDING_VAR_1
-->
This scheduled prompt has not run yet, because it may need the user's approval. To run it, call the ${SYSTEM_REMINDER_SCHEDULED_PROMPT_SKILL_APPROVAL_PENDING_VAR_0} tool for ${SYSTEM_REMINDER_SCHEDULED_PROMPT_SKILL_APPROVAL_PENDING_VAR_1.join(", then for ")}, with the prompt's arguments. If the call is refused, do not do the skill's work another way.
