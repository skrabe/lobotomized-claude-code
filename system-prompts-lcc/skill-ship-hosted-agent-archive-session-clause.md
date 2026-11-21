<!--
name: 'Ship: Hosted Agent Archive Session Clause'
description: >-
  Clause in the /ship take-over instructions telling the user to archive the
  cloud session at the Claude Code web URL when another hosted agent holds the
  PR.
ccVersion: 2.1.330
variables:
  - SKILL_SHIP_HOSTED_AGENT_ARCHIVE_SESSION_CLAUSE_VAR_0
  - SKILL_SHIP_HOSTED_AGENT_ARCHIVE_SESSION_CLAUSE_VAR_1
-->
archive that session at ${SKILL_SHIP_HOSTED_AGENT_ARCHIVE_SESSION_CLAUSE_VAR_0()}/code if ${SKILL_SHIP_HOSTED_AGENT_ARCHIVE_SESSION_CLAUSE_VAR_1===void 0?"there is one":"it hasn't ended"}, 
