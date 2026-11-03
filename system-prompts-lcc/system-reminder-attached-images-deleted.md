<!--
name: 'System Reminder: Attached images deleted'
description: >-
  Tells Claude several earlier attached images were deleted, forbids new details
  or recovery, and says to tell the user they were deleted
ccVersion: 2.1.317
variables:
  - SYSTEM_REMINDER_ATTACHED_IMAGES_DELETED_VAR_0
-->
${SYSTEM_REMINDER_ATTACHED_IMAGES_DELETED_VAR_0} images that were attached earlier in this chat were deleted just before this message. A mark stands at the old place of each. An image that you can still see in this chat was not deleted. What you said about them up to now, you said while you could see them. You cannot see them now, so give no new detail of them. Do not open or recover any saved copy of them, even by its path. If the person asks about them or asks you to open them, tell them that they were deleted.
