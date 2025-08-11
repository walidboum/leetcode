# 317. Shortest Distance from All Buildings

**Source:** [https://leetcode.ca/all/317.html](https://leetcode.ca/all/317.html)

**Companies:** Amazon, ByteDance, Facebook, Goldman Sachs, Google, Mathworks, Microsoft, Snapchat, Splunk, Uber, Zenefits

## Description

You want to build a house on an

empty

land which reaches all buildings in the shortest
        amount of distance. You can only move up, down, left and right. You are given a 2D grid of
        values

0

,

1

or

2

, where:

Each

0

marks an empty land which you can pass by freely.

Each

1

marks a building which you cannot pass through.

Each

2

marks an obstacle which you cannot pass through.

## Examples

### Example

```
Example:
Input:
[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
Output:
7
Explanation:
Given three buildings at
(0,0)
,
(0,4)
,
(2,2)
, and an obstacle at
(0,2),
             t
he point
(1,2)
is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to
        the above rules, return -1.
```

