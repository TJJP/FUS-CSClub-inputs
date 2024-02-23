# Flatten Map
Given a file with a map of strings to strings, output a "flattened" version of that map. The number of 
pairs is at the start. The keys are guaranteed to be unique, but the values may repeat. Example:
```
11
mother punishment
warm cushion
fact fear
punishment cow
steel steel
prose time
time punishment
fear prose
short existence
cushion steel
cow banana
```
becomes
```
mother banana
warm steel
fact banana
punishment banana
UB
prose banana
time banana
fear banana
short existence
cushion steel
cow banana
```
Note the UB - any mappings of a key to itself may be discarded, and it mostly does not matter what is on that
line (there still has to be some non-whitespace character, or the verifier won't run properly). By the end,
none of the values should be keys.

