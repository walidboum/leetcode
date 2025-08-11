# 311. Sparse Matrix Multiplication

**Source:** [https://leetcode.ca/all/311.html](https://leetcode.ca/all/311.html)

**Companies:** Amazon, Apple, Bloomberg, Facebook, Goldman Sachs, Google, LinkedIn, Microsoft, Snapchat

## Description

Given two

sparse
        matrices

A

and

B

, return the result of

AB

.

You may assume that

A

's column number is equal to

B

's row number.

## Examples

### Example

```
Example:
Input:
A
= [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B
= [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
Output:
|  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB
= | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
```

