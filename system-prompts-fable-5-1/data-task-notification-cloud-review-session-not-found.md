<!--
name: 'Data: Task Notification Cloud Review Session Not Found'
description: >-
  Trailing instruction on a failed cloud-review task notification when the
  review session is missing under the signed-in account.
ccVersion: 2.1.280
-->
Tell the user that plainly. If they signed in to a different account or organization, the review may still finish under the one that started it; signing back in as that account first and then resuming this conversation (claude --resume) re-attaches it if it is still there. Do not start another review, cloud or local, unless the user asks.
