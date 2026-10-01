<!--
name: 'Tool Parameter: Artifact action share'
description: >-
  Artifact tool action parameter clause for share: shares with the whole
  organization or named people in it, the user confirms on a card, never public
ccVersion: 2.1.286
-->
 'share' shares an artifact the user owns with their whole organization or with named people in it (pass `url`, `mode` 'org' or 'people', `people` — names or emails, hints the host resolves — for 'people', and for 'people' `access` 'view' or 'comment', default 'comment'; nothing else may accompany it) — the user reviews and confirms every share on a card and may change the audience there; never public, never people outside the organization. See **Sharing** below.
