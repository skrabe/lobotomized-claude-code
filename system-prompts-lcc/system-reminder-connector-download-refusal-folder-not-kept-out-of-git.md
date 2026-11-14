<!--
name: 'System Reminder: Connector download refusal - folder not kept out of git'
description: 'Refusal reason: the folder''s .gitignore doesn''t ignore everything.'
ccVersion: 2.1.325
-->
the connector-downloads folder has a .gitignore that doesn't ignore everything (an empty one can be left by an earlier save that stopped partway), so connector files aren't saved there; the person can remove that .gitignore, then run the tool again
