<!--
name: 'Tool Parameter: Self-hosted runner requeue runner id'
description: >-
  Input-schema description of the runner_id parameter of the
  self_hosted_runner_requeue_session tool.
ccVersion: 2.1.316
-->
Tagged runner id (ccrunner_…) the caller observed failing. Server verifies this still matches the session assignment; mismatch returns Conflict. For a stuck session with no runner assigned, pass any runner id of this environment, such as one of the excluded_runner_ids of the session; the server does not compare it.
