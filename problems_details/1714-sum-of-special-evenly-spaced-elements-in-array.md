# 1714. Sum Of Special Evenly-Spaced Elements In Array

**Source:** [https://leetcode.ca/all/1714.html](https://leetcode.ca/all/1714.html)

**Companies:** MakeMyTrip, Sprinklr

## Description

You are given a

0-indexed

integer array

nums

consisting of

n

non-negative integers.

You are also given an array

queries

, where

queries[i] =
                [x

i

, y

i

]

. The answer to the

i

th

query is the sum of all

nums[j]

where

x

i

<= j <
                    n

and

(j - x

i

)

is divisible by

y

i

.

Return

an array

answer

where

answer.length ==
                queries.length

and

answer[i]

is the answer to
                the

i

th

query

modulo

10

9

+ 7

.

Example 1:

Input:

nums = [0,1,2,3,4,5,6,7], queries = [[0,3],[5,1],[4,2]]

Output:

[9,18,10]

Explanation:

The answers of the queries are as follows:
1) The j indices that satisfy this query are 0, 3, and 6. nums[0] + nums[3] + nums[6] = 9
2) The j indices that satisfy this query are 5, 6, and 7. nums[5] + nums[6] + nums[7] = 18
3) The j indices that satisfy this query are 4 and 6. nums[4] + nums[6] = 10

Example 2:

Input:

nums = [100,200,101,201,102,202,103,203], queries = [[0,7]]

Output:

[303]

Constraints:

n == nums.length

1 <= n <= 5 * 10

4

0 <= nums[i] <= 10

9

1 <= queries.length <= 1.5 * 10

5

0 <= x

i

< n

1 <= y

i

<= 5 * 10

4

Difficulty:

Hard

Lock:

Prime

Company:

MakeMyTrip

Sprinklr

Problem Solution

1714-Sum-Of-Special-Evenly-Spaced-Elements-In-Array

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly
        every week. They are for personal study and research only, and should not be used for
        commercial purposes. Thank you for your cooperation.

