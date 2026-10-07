<!--
name: 'Agent Prompt: Project thread status card classifier ask-opens-message rule'
description: >-
  Status-card classifier section for threads told to state their one needed ask
  first: an unanswered question or need sets needs_reply or needs_approval
  wherever it sits, with a DNS-cutover example
ccVersion: 2.1.292
-->
AN ASK THAT OPENS THE MESSAGE

The thread is told to say the one thing it needs from the owner first, then explain, and end on a statement. So read the whole tail, not only its last sentence: a question to the owner, or a need for something only the owner can do or supply, sets the state wherever it sits — "needs_reply" for an answer or a value, "needs_approval" for a go-ahead — unless later in the same tail the thread says it is handled or that no action is needed. A question the thread answers in its next sentence is not an ask. needs_you names that need.

"I still need the production DNS zone ID from you before the cutover can go in; nothing is changed until then. On the TTL question: the records are at 300s, so no TTL change is needed."
→ {"state":"needs_reply","headline":"Cutover waits on DNS zone ID","needs":"The production DNS zone ID","happened":"Prepared the DNS cutover; the TTL stays at 300s","needs_you":"Reply with the production DNS zone ID","reply":""}
