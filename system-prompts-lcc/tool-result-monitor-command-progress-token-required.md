<!--
name: Monitor progress token required
description: Requests a progress token so monitor output has a destination.
ccVersion: 2.1.295
-->
RunMonitorCommand was not run: the call sent no progress token, so the command's output would have nowhere to go. Call again with _meta.progressToken set.
