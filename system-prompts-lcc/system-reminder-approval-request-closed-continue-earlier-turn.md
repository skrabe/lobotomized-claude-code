<!--
name: 'System reminder: closed approval request, continue earlier turn'
description: >-
  Meta prompt telling the model to resume an earlier turn whose approval was
  closed by an automatic message.
ccVersion: 2.1.322
-->
An approval request of an earlier turn was closed unanswered when an automatic message arrived, so that turn was left unfinished. The automatic message is dealt with now. Continue that earlier turn from where it stopped: if the action or actions that awaited approval are still needed, make the same call again, so that the user can approve it. If they are no longer needed, say in one plain sentence which action did not run.
