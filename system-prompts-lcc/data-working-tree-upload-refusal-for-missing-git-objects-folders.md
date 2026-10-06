<!--
name: 'Data: Working tree upload refusal for missing git objects folders'
description: >-
  Error refusing a working-tree upload because the git directory lacks
  objects/info or objects/pack, as after a copy that skips empty folders,
  telling the user to check for links with ls -ld and then recreate both with
  mkdir, or start from a fresh clone
ccVersion: 2.1.291
-->
This checkout’s git directory lacks objects/info or objects/pack, so nothing was uploaded. Git makes both in every repository and works without them; a copy that skips empty folders loses them. To make them again, in an ordinary checkout, at its top level, where .git is: first look with ls -ld .git .git/objects (a link shows an arrow, ->). If either is a link, stop, since the folders would be made wherever it points, and start from a fresh clone instead. Otherwise run mkdir .git/objects/info .git/objects/pack (an error that one of them exists does no harm), then retry.
