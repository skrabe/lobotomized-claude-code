<!--
name: 'Data: allowManagedPermissionRulesOnly setting description (part 2 of 3)'
description: >-
  Description of the `allowManagedPermissionRulesOnly` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.325
-->
The allowed-tools frontmatter of skills and custom commands from user, project, and --add-dir sources, and of plugins no managed setting vouches for, is ignored too. Plugins keep theirs only on an admin-backed channel: host-delivered --plugin-dir plugins (in Claude Desktop, only while this is not set by the organization's own managed settings), the official marketplace registered from its unpinned anthropics source, claude.ai-synced plugins Anthropic attests, the saved login organization's claude.ai-hosted marketplaces, marketplaces whose registered source managed extraKnownMarketplaces declares or an exact or owner-pinned (owner/*) strictKnownMarketplaces entry names at the path it pins (an npm marketplace source only when the registration and the declared entry pin the same registry, and a settings marketplace source only when every nested npm plugin entry pins one on a bare package name — unpinned, the package resolves through the member's own npm config, and a non-bare spelling packs as an exotic spec the pin does not bind, so nothing an entry names is what was fetched) (host and path patterns and enabledPlugins ids do not vouch); managed and bundled skills keep theirs. 
