Adding Numbers Design Document
==============================

The purpose of this document is to describe the design for Module 28 - Adding Numbers

```flow
st=>start
e=>end
init=>operation: Initialize counter and sum to 0
add=>operation: Prompt number and add to sum
inc=>operation: Increment counter
cond=>condition: counter less than 5?:
st->init->cond
cond(yes)->add->inc(left)->cond
cond(no)->e
```

[flowchart.js.org](http://flowchart.js.org/)
