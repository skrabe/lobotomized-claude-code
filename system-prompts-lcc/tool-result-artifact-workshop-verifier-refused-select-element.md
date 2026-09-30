<!--
name: 'Tool Result: Workshop verifier refuses select element'
description: >-
  Hint in the workshop page structural-verifier refusal saying select is not
  allowed because markup inside it would go uninspected, and to mock the control
  up with a list or buttons
ccVersion: 2.1.285
-->
<select> is not allowed — browsers and this verifier parse its contents differently, so markup inside it would go uninspected. Mock up the control with a list or buttons instead.
