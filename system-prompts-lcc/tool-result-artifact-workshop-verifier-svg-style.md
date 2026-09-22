<!--
name: 'Workshop Verifier: Style Inside SVG'
description: >-
  Verifier violation hint returned when a workshop page places a <style> element
  inside SVG.
ccVersion: 2.1.219
-->
Remove it — <style> inside SVG is a serialization-hazard surface (mutation-XSS carrier); use the page-level <style> block or SVG presentation attributes.
