<!--
name: 'Tool Description: Computer request_access'
description: >-
  Describes the computer-use request_access tool for asking user permission to
  control applications in the session
ccVersion: 2.1.178
-->
Request user permission to control a set of applications for this session. Must be called before any other tool in this server. The user sees a single dialog listing all requested apps and either allows the whole set or denies it. Call this again mid-session to add more apps; previously granted apps remain granted. Returns the granted apps, denied apps, and screenshot filtering capability.
