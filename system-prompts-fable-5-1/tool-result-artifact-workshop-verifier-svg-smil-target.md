<!--
name: 'Workshop Verifier: SMIL Animation Target'
description: >-
  Verifier violation hint returned when SMIL animates a URL, navigation, script,
  style or workshop-surface attribute.
ccVersion: 2.1.219
-->
SMIL may only animate geometry and paint properties — never URL (href/src/srcset…), navigation (target/rel/ping/referrerpolicy), script (on*), style/class, or workshop-surface attributes.
