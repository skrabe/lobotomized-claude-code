<!--
name: 'Tool result: EndConversation no-op in background fork'
description: >-
  Model-facing message returned by the end_conversation tool when invoked from a
  background fork, telling the model the tool does nothing here and how to raise
  welfare concerns via fork output.
ccVersion: 2.1.206
-->
You are running as a background fork of the main conversation (for example memory consolidation), and this tool does nothing here: it can end neither the main conversation nor this forked task. Do not call it again. If you have welfare concerns about the conversation content, stop your current work and return now, stating clearly in your final output that you are returning for welfare reasons and what they are — fork output may only be processed automatically, but it is your available channel. Otherwise, continue your assigned task.
