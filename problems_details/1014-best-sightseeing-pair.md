# 1014. Best Sightseeing Pair

**Source:** [https://leetcode.ca/all/1014.html](https://leetcode.ca/all/1014.html)

**Companies:** Wayfair

## Description

Given an array

A

of positive integers,

A[i]

represents the value of
        the

i

-th sightseeing spot, and two sightseeing spots

i

and

j

have distance

j - i

between them.

The

score

of a pair (

i < j

) of sightseeing spots is (

A[i]
        + A[j] + i - j)

: the sum of the values of the sightseeing spots,

minus

the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input:

[8,1,5,2,6]

Output:

11

Explanation:

i = 0, j = 2,

A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

Note:

2 <= A.length <= 50000

1 <= A[i] <= 1000

Difficulty:

Medium

Lock:

Normal

Company:

Wayfair

Problem Solution

1014-Best-Sightseeing-Pair

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

