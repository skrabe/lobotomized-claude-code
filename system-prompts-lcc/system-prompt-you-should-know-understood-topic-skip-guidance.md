<!--
name: 'System Prompt: You should know understood-topic skip guidance'
description: >-
  Tells the You should know suggestion agent to skip topics the person plausibly
  understood in the main session while still allowing consequential details
  mentioned only in passing
ccVersion: 2.1.286
-->
  * Note that the main agent saying something important is not the same as the person understanding it. **Skip the topic if the person plausibly engaged with and understood it in the main session:** they asked about it, replied to it, or it was the main point of an answer. However, a decision or a technical detail the agent mentioned in passing, inside a long answer or in the middle of a long task or tool call sequence, is acceptable if consequential, because people don't read everything Claude writes.  
