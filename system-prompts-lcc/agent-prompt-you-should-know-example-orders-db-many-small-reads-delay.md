<!--
name: 'You should know example: Orders DB small-read delay'
description: >-
  GOOD-example bullet explaining that frequent small reads multiply the
  decryption delay
ccVersion: 2.1.286
-->
* If the Orders DB reads many small records often, that extra step happens many times per request and can add delay.  
