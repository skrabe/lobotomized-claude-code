<!--
name: 'Plugin validate: dynamic import() in a hooks module'
description: >-
  Hooks-module scan refusal for a dynamic import(): a hooks module imports its
  own files with an import declaration, as in import { name } from "./file.js".
ccVersion: 2.1.288
-->
a dynamic import(); a hooks module imports its own files with an import declaration, as in import { name } from "./file.js"
