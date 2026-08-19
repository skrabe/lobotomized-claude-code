<!--
name: 'Tool Result: resume_replies denied — the artifact''s watch is stopped'
description: >-
  Denial returned when resume_replies is called for an artifact whose watch was
  stopped earlier in the session: there is no separate auto-reply stop to
  resume, and the watch action must be used instead.
ccVersion: 2.1.235
-->
Automatic replies are off for this artifact because watching it was stopped earlier in this session — there is no separate auto-reply stop to resume. If the user wants them back, call the watch action for this artifact (which may ask before re-arming the watch); replies return with the next publish after that. Nothing here needs approval.
