<!--
name: 'Connector download refusal: unattended'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because cloud sessions skip downloads for unattended tool calls.
ccVersion: 2.1.319
-->
in a cloud session, files aren't downloaded for a tool call that runs in the background (a background subagent's included), for a teammate, inside a script, or in a run a trigger started, and this one did; calling the tool directly in a session a person started may work
