<!--
name: 'System prompt: memory sync not running under policy'
description: >-
  Memory section note that memory sync was not running when the prompt was built
  and how writes behave while policy keeps it stopped.
ccVersion: 2.1.325
-->
Memory sync was not running when this prompt was built, because the organization's policy had not loaded or did not allow it, so the memory directories may lack other sessions' notes. Sync may have started since. While the policy keeps it stopped, a Write or Edit that would otherwise sync stays on this machine, whatever this section says about syncing, and returns a warning. If sync starts later, such a write can still be uploaded, so this section's rules on what to save still apply.
