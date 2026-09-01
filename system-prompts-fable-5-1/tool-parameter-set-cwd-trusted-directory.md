<!--
name: Set Cwd Trusted Directory Param
description: >-
  Model-facing input-schema description for the set_cwd control tool's
  trusted_directory parameter.
ccVersion: 2.1.201
-->
Required whenever trust_accepted is true: the exact directory string from the needs_trust response being answered. This pins the attestation to the canonical path the user was shown — if the raw path canonicalizes differently by the time the re-send arrives (e.g. a symlink component changed during the dialog), nothing is latched and a fresh needs_trust carries the new canonical directory.
