<!--
name: Bash find -regex note
description: Bash tool description bullet on find -regex alternation ordering.
ccVersion: 2.1.206
-->
When using `find -regex` with alternation, put the longest alternative first. Example: use `'.*\.\(tsx\|ts\)'` not `'.*\.\(ts\|tsx\)'` — the second form silently skips `.tsx` files.
