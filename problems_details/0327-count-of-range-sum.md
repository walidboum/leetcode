# 327. Count of Range Sum

**Source:** [https://leetcode.ca/all/327.html](https://leetcode.ca/all/327.html)

**Companies:** Google

## Description

Given an integer array

nums

, return the number of range sums that lie in

[lower,
        upper]

inclusive.

Range sum

S(i, j)

is defined as the sum of the elements in

nums

between indices

i

and

j

(

i

≤

j

),
        inclusive.

Note:

A naive algorithm of

O

(

n

2

) is trivial. You MUST do better than
        that.

## Examples

### Example

```
Example:
Input:
nums
=
[-2,5,-1]
,
lower
=
-2
,
upper
=
2
,
Output:
3
Explanation:
The three ranges are :
[0,0]
,
[2,2]
,
[0,2]
and their respective sums are:
-2, -1, 2
.
```

