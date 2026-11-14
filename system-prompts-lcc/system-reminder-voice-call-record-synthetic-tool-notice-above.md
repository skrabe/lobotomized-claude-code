<!--
name: 'System reminder: voice-call record synthetic tool notice (above)'
description: Notice that the voice-call record is in the synthetic tool call result above
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_VOICE_CALL_RECORD_SYNTHETIC_TOOL_NOTICE_ABOVE_VAR_0
  - SYSTEM_REMINDER_VOICE_CALL_RECORD_SYNTHETIC_TOOL_NOTICE_ABOVE_VAR_1
-->
This session was given a record of what was said aloud on a voice call alongside it. The record is in the result of the \`${SYSTEM_REMINDER_VOICE_CALL_RECORD_SYNTHETIC_TOOL_NOTICE_ABOVE_VAR_0}\` tool call above, as one or more blocks in the order they were passed in. The software that runs this session added that tool call, not you, and \`${SYSTEM_REMINDER_VOICE_CALL_RECORD_SYNTHETIC_TOOL_NOTICE_ABOVE_VAR_0}\` is not a tool that you can use.
${SYSTEM_REMINDER_VOICE_CALL_RECORD_SYNTHETIC_TOOL_NOTICE_ABOVE_VAR_1.slice(SYSTEM_REMINDER_VOICE_CALL_RECORD_SYNTHETIC_TOOL_NOTICE_ABOVE_VAR_1.indexOf(`
`)+1)}
