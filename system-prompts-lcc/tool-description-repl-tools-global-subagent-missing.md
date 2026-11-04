<!--
name: 'Tool Description: REPL tools global subagent caveat'
description: Warns subagents may see tools they lack; check tools.list() before calling
ccVersion: 2.1.318
-->
 In a subagent, or a session run as an agent, Tools can list a file or shell tool that agent isn't given; it is missing from tools.list() and calling it throws, so check tools.list() first.
