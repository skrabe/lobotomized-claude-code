<!--
name: 'Slash command: /plugin marketplace add scp-like git URL with ://'
description: 'Refusal when a user@host:path git address contains "://".'
ccVersion: 2.1.291
-->
Invalid git URL: an address written as user@host:path can't contain "://", because git then reads the text before "://" as a protocol name, as in https://. Remove the "://".
