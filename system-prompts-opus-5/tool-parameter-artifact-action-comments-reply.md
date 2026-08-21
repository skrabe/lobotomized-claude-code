<!--
name: Artifact Action Parameter — Comments And Reply
description: >-
  Clause appended to the Artifact tool's `action` enum .describe() text
  explaining the 'comments' and 'reply' actions; ships in the tool's input
  schema to the model.
ccVersion: 2.1.238
-->
activation can also be cleared — by deactivating Claude on the thread, or by the thread being deleted — but survives a republish or rename, and is unrelated to whether a thread is resolved (resolved threads still accept replies). Resolve, like reply, works only on threads activated for Claude: never call resolve on a thread marked NOT activated, even one you addressed — tell the user what you did and leave that thread for the commenter to resolve.
