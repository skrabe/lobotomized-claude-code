<!--
name: 'Tool Description: LSP'
description: Description for the LSP tool.
ccVersion: 2.1.162
-->
Interact with Language Server Protocol (LSP) servers for code intelligence.

Operations:
- goToDefinition: where a symbol is defined
- findReferences: all references to a symbol
- hover: documentation / type info for a symbol
- documentSymbol: all symbols (functions, classes, variables) in a document
- workspaceSymbol: search symbols across the workspace
- goToImplementation: implementations of an interface or abstract method
- prepareCallHierarchy: call-hierarchy item at a position
- incomingCalls: functions/methods that call the function at a position
- outgoingCalls: functions/methods called by the function at a position

All operations require filePath, line, and character (line/character are 1-based, as shown in editors).

An LSP server must be configured for the file type, otherwise an error is returned.
