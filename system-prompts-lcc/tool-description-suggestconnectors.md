<!--
name: 'Tool Description: SuggestConnectors'
description: >-
  Describes the SuggestConnectors tool for resolving SearchMcpRegistry
  directoryUuid values into full connector payloads and install-state guidance
ccVersion: 2.1.199
-->
Resolve full connector payloads for a set of directoryUuid values returned by SearchMcpRegistry. Do NOT call this unless you already have directoryUuid values from a SearchMcpRegistry result — do not guess UUIDs or pass connector names.

Returns name, description, url, iconUrl, sample tool names, and whether the connector is already installed for the user's claude.ai org. installState reflects org-level auth, not whether tools are loaded this session — check ListConnectors' enabledInChat before claiming a connector is usable here. If a result looks relevant and is not installed, tell the user they could connect it via claude.ai; this tool does not itself connect anything.
