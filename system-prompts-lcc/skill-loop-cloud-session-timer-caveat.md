<!--
name: 'Skill: /loop cloud session timer caveat'
description: >-
  Warns that a /loop timer in a cloud session lives in a releasable container
  and asks for a one-sentence note in the confirmation
ccVersion: 2.1.319
-->

## This is a cloud session

A timer set here lives in this session's container. It fires only while that container is up: the container can be released while the session is idle or replaced at any time, and a new container does not re-arm the timer.

In your confirmation, tell the user this in one sentence.
