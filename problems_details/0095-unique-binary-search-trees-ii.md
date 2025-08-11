# 95. Unique Binary Search Trees II

**Source:** [https://leetcode.ca/all/95.html](https://leetcode.ca/all/95.html)

**Companies:** Adobe, Apple, Google, Microsoft, Yahoo

## Description

Given an integer

n

, generate all structurally unique

BST's

(binary search trees) that store values 1 ...

n

.

## Examples

### Example

```
Example:
Input:
3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

