<!--
name: 'REPL: Script Stopped Before Start'
description: >-
  REPL failure when the script's report never arrived, using the lost message or
  saying the script was stopped before it started.
ccVersion: 2.1.331
-->
REPL: ${this.#r.messages.lost??"the script was stopped before it started"}
