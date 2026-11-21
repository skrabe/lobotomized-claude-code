<!--
name: 'Plugin Error: Repository Refused (Not In Session)'
description: >-
  Plugin fetch error reason saying the repository isn't one of the session's
  repositories and how to add it.
ccVersion: 2.1.330
variables:
  - DATA_PLUGIN_ERROR_REPOSITORY_REFUSED_NOT_IN_SESSION_VAR_0
  - DATA_PLUGIN_ERROR_REPOSITORY_REFUSED_NOT_IN_SESSION_VAR_1
  - DATA_PLUGIN_ERROR_REPOSITORY_REFUSED_NOT_IN_SESSION_VAR_2
-->
${DATA_PLUGIN_ERROR_REPOSITORY_REFUSED_NOT_IN_SESSION_VAR_0(DATA_PLUGIN_ERROR_REPOSITORY_REFUSED_NOT_IN_SESSION_VAR_1)} isn't one of this session's repositories${DATA_PLUGIN_ERROR_REPOSITORY_REFUSED_NOT_IN_SESSION_VAR_2.ofSubmodule?"":", or the marketplace names it wrong"}. If your access and your organization allow it, you can choose that repository when you start a session, or ask Claude to add that repository to this session.
