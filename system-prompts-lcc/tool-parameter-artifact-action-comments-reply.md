<!--
name: Artifact Action Parameter — Comments And Reply
description: >-
  Clause appended to the Artifact tool's `action` enum .describe() text
  explaining the 'comments' and 'reply' actions; ships in the tool's input
  schema to the model.
ccVersion: 2.1.251
-->
activation can later be gone (Claude's access revoked, or the thread deleted) but survives a republish or rename, and is unrelated to whether a thread is resolved (resolved threads still accept replies). Resolve, like reply, works only on threads activated for Claude: never call resolve on a thread marked NOT activated, even one you addressed — it stays open; tell the user which threads remain open because they are not sent to Claude, and that a writer can send one to Claude (reply on it with Send to Claude) or resolve it in the artifact view.
