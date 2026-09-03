<!--
name: 'Tool Parameter: Artifact Comments Action'
description: >-
  Input-schema describe() for the comments-tool action enum covering read,
  reply, resolve, and watch.
ccVersion: 2.1.257
-->
'read' reads the comment threads on the artifact at `url` (add `thread_id` for one thread, or `cursor` to continue a listing); 'reply' posts `text` into the thread `thread_id`; 'resolve' marks that thread resolved; 'watch' manages this session's artifact watches — with `url` it starts watching that artifact (`on: false` stops), with no `url` it lists this session's watches and rooms
