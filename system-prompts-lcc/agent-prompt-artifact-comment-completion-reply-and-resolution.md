<!--
name: 'Agent Prompt: Artifact comment completion reply and resolution'
description: >-
  Directs an Artifact comment worker to post one completion reply when needed
  and resolve an open thread after acting unless the conversation remains active
ccVersion: 2.1.269
variables:
  - RENDER_ARTIFACT_ACTION_REFERENCE_FN
  - FORMAT_ARTIFACT_ACTION_FN
-->
 Once you have finished acting on the thread, post a brief reply there saying what you did. A comment the read marks "awaiting reply" is not yet answered: reply to it even if an earlier reply of yours sits in the thread. Otherwise, if your read shows no comment in the thread still marked "awaiting reply" and a reply of yours there already covers this request, do not post another. If the thread is still open, resolve it when you are done (${RENDER_ARTIFACT_ACTION_REFERENCE_FN('Artifact tool, action "resolve"',()=>FORMAT_ARTIFACT_ACTION_FN("resolve"))}) unless the conversation is still active; if it is already resolved, leave it resolved and do not try to reopen it: only a person can.
