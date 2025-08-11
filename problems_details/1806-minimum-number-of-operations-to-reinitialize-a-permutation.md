# 1806. Minimum Number of Operations to Reinitialize a Permutation

**Source:** [https://leetcode.ca/all/1806.html](https://leetcode.ca/all/1806.html)

**Companies:** Google

## Description

You are given an

even

integer

n

ââââââ. You initially have a permutation

perm

of size

n

ââ where

perm[i] == i

â

(0-indexed)

ââââ.

In one operation, you will create a new array

arr

, and for each

i

:

If

i % 2 == 0

, then

arr[i] = perm[i / 2]

.

If

i % 2 == 1

, then

arr[i] = perm[n / 2 + (i - 1) / 2]

.

You will then assign

arr

ââââ to

perm

.

Return

the minimum

non-zero

number of operations you need to perform on

perm

to return the permutation to its initial value.

Example 1:

Input:

n = 2

Output:

1

Explanation:

perm = [0,1] initially.
After the 1

st

operation, perm = [0,1]
So it takes only 1 operation.

Example 2:

Input:

n = 4

Output:

2

Explanation:

perm = [0,1,2,3] initially.
After the 1

st

operation, perm = [0,2,1,3]
After the 2

nd

operation, perm = [0,1,2,3]
So it takes only 2 operations.

Example 3:

Input:

n = 6

Output:

4

Constraints:

2 <= n <= 1000

n

ââââââ is even.

Difficulty:

Medium

Lock:

Normal

Company:

Google

Problem Solution

Leetcode Solutions Java Python C++

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

