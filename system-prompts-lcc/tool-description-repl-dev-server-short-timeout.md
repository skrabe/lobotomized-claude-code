<!--
name: 'Tool Description: REPL dev server via short timeout'
description: >-
  REPL prompt guidance to keep a dev server running by awaiting it with a short
  timeout instead of nohup/setsid/&
ccVersion: 2.1.328
-->
 To keep a dev server or a watcher running, await it with a short timeout: `const server = await $`npm run dev`.timeout(3000)` moves it to the background after 3 s, where the user can see and stop it, and `server.running.outputPath` names the file with its output. Don't use `nohup`, `setsid` or `&` for this: Claude Code can't show or stop what they start.
