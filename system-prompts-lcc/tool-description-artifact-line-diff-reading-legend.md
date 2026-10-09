<!--
name: 'Tool Description: Artifact line diff reading legend'
description: >-
  Legend for the live-page line diff in a stale Artifact publish refusal,
  explaining the column-1 marks (+, -, space, ~), the @@ hunk header and the
  block ids that publish stamps on /doc pages
ccVersion: 2.1.295
-->
How to read the diff: every line of it starts with a one-character mark in column 1 — "+" marks a line that is on the live page and not in what you sent (your next publish must carry it, unless removing it is what you intend); "-" marks a line that is only in what you sent (your own edit, to keep — or a line the other writer removed, so check it against what you changed); " " marks an unchanged line shown for context ("~" one too long to show, named instead); "@@ -a,b +c,d @@" gives the approximate position in your content, then in the live page (locate by the context lines). Every line not shown is identical in both; on a /doc page the lines shown carry the block ids publish stamps, which your file may lack.
