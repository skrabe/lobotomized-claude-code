<!--
name: 'Tool Description: Poll declared event kinds intro'
description: >-
  Poll tool prompt block listing the event kinds the host declares: each is
  returned as an event element whose body is one JSON object with the listed
  fields; the host sets every field except those marked untrusted.
ccVersion: 2.1.288
variables:
  - TOOL_DESCRIPTION_POLL_DECLARED_EVENT_KINDS_INTRO_VAR_0
  - TOOL_DESCRIPTION_POLL_DECLARED_EVENT_KINDS_INTRO_VAR_1
  - TOOL_DESCRIPTION_POLL_DECLARED_EVENT_KINDS_INTRO_VAR_2
-->
Your host declares the event kinds below. Poll returns each one as an event element whose body is one JSON object, with only the fields listed for its kind. ${TOOL_DESCRIPTION_POLL_DECLARED_EVENT_KINDS_INTRO_VAR_0} The host sets every field except those listed as untrusted, which may hold text from untrusted sources.
${TOOL_DESCRIPTION_POLL_DECLARED_EVENT_KINDS_INTRO_VAR_1(TOOL_DESCRIPTION_POLL_DECLARED_EVENT_KINDS_INTRO_VAR_2)}
