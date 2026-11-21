<!--
name: 'Tool Result: Steward replace refs or grafts'
description: Refuses every base merge when the checkout holds git replace refs or grafts
ccVersion: 2.1.330
-->
this checkout holds replace refs (git replace -l) or grafts (.git/info/grafts), so the merge might not bring what GitHub holds for that commit. Leave every merge of the base to the user
