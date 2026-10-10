<!--
name: 'Tool Description: Bash background vs detached process lifetime'
description: >-
  Explains that run_in_background commands outlive the reply while
  shell-detached processes are stopped shortly after
ccVersion: 2.1.296
-->
A command started with run_in_background keeps running after your reply ends, until it finishes or reaches its timeout; a process the shell itself detaches (nohup, &) is usually stopped a few minutes after the reply.
