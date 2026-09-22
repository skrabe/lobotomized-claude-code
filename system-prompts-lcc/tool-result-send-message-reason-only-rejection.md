<!--
name: Reason only on rejection
description: SendMessage validation error returned to the model about the reason field.
ccVersion: 2.1.206
-->
reason is only delivered on rejections (approve: false) — approvals are sent as a silent confirmation with no reason text; omit reason or reject instead
