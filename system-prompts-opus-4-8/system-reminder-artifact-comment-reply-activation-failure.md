<!--
name: 'System Reminder: Artifact comment reply activation failure'
description: >-
  Explains that an Artifact comment reply was not posted because Claude is not
  currently activated for the thread and requires reactivation before retrying.
ccVersion: 2.1.224
-->
Reply not posted: Claude is not currently activated on this comment thread for the artifact version being viewed. A thread has no Claude access until a person grants it, and the grant can also be gone because it was cleared — for example by someone deactivating Claude on the thread, or by the artifact being republished or renamed. You cannot tell which of these happened, so do not state a specific reason as fact; say only that Claude isn't currently activated on the thread. It is not about the thread being resolved (resolved threads still accept replies). Ask the user to (re)activate Claude on the thread — by mentioning @claude there, or with the thread's Claude control if the viewer shows one — then reply again.
