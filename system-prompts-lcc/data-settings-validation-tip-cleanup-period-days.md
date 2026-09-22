<!--
name: 'Data: settings validation tip (cleanupPeriodDays below 1)'
description: >-
  Suggestion appended to a settings.json validation error (cleanupPeriodDays
  below 1); the model reads it in the tool result when its edit to a settings
  file fails validation.
ccVersion: 2.1.276
-->
cleanupPeriodDays must be at least 1. To keep transcripts for a long time, set a large number (e.g. 3650 for ~10 years). To disable transcript writes entirely, remove this setting and use the --no-session-persistence CLI flag or the SDK persistSession:false option instead. (0 is rejected because it previously silently disabled all transcript writes, which users setting it to mean "never clean up" did not expect.)
