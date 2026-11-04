<!--
name: 'System Reminder: Sandbox guidance for REPL $ shell'
description: >-
  Addition to the sandbox attachment in REPL mode explaining that $ and the
  shell tool both run commands and how to pass dangerouslyDisableSandbox.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_SANDBOX_REPL_DOLLAR_DISABLE_SANDBOX_VAR_0
  - SYSTEM_REMINDER_SANDBOX_REPL_DOLLAR_DISABLE_SANDBOX_VAR_1
-->
${SYSTEM_REMINDER_SANDBOX_REPL_DOLLAR_DISABLE_SANDBOX_VAR_0}

In a REPL script, \`$\` and \`${SYSTEM_REMINDER_SANDBOX_REPL_DOLLAR_DISABLE_SANDBOX_VAR_1}\` both run ${SYSTEM_REMINDER_SANDBOX_REPL_DOLLAR_DISABLE_SANDBOX_VAR_1} tool commands. Where the text above allows \`dangerouslyDisableSandbox: true\`, pass it as \`${SYSTEM_REMINDER_SANDBOX_REPL_DOLLAR_DISABLE_SANDBOX_VAR_1}({command, dangerouslyDisableSandbox: true})\`: \`$\` has no option for it.
