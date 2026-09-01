<!--
name: 'Auto-Mode Recon: classifyAllShell Note'
description: >-
  Markdown note explaining classifyAllShell makes auto mode ignore all shell
  allow rules; a fragment of the /auto-mode-setup recon context injected into
  the model.
ccVersion: 2.1.207
-->

_Note: classifyAllShell is active, so at runtime auto mode ignores every Bash/PowerShell allow rule — a superset of the entries flagged here, including any shell entries in the destructive list; outside auto mode all of these rules still apply._
