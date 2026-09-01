<!--
name: PowerShell tool description — verified dev tools on PATH
description: >-
  Fragment of the PowerShell Bash tool description listing developer tools
  verified on this machine's PATH and how to probe for unlisted ones.
ccVersion: 2.1.199
variables:
  - TOOL_DESCRIPTION_POWERSHELL_VERIFIED_DEV_TOOLS_VAR_0
  - TOOL_DESCRIPTION_POWERSHELL_VERIFIED_DEV_TOOLS_VAR_1
-->

Developer tools verified on this machine's PATH: ${TOOL_DESCRIPTION_POWERSHELL_VERIFIED_DEV_TOOLS_VAR_0.join(", ")}
   - Prefer these. A build/dev tool NOT in this list is likely not installed — do not assume \`make\`, \`gcc\`, or a package manager is available unless listed. Check with \`if (Get-Command <name> -ErrorAction SilentlyContinue) { ... }\` before relying on an unlisted tool, and prefer a listed equivalent.${TOOL_DESCRIPTION_POWERSHELL_VERIFIED_DEV_TOOLS_VAR_1}
