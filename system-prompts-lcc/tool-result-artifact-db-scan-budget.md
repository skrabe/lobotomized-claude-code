<!--
name: 'Tool Result: Artifact DB scan budget exceeded'
description: Collection too large to sort; drop query.order_by and page with query.cursor
ccVersion: 2.1.322
-->
this collection holds too much data to sort, whatever `query.where` or `query.limit` you pass — drop `query.order_by`, page with `query.cursor` and sort the results yourself; an ordered query will keep failing until the collection holds fewer or smaller documents
