# 1735. Count Ways to Make Array With Product

**Source:** [https://leetcode.ca/all/1735.html](https://leetcode.ca/all/1735.html)

**Companies:** Amazon

## Description

You are given a 2D integer array,

queries

. For each

queries[i]

, where

queries[i] = [n

i

, k

i

]

,
            find the number of different ways you can place positive integers into an array of size

n

i

such that the product of the integers is

k

i

.
            As the number of ways may be too large, the answer to the

i

th

query is the number of ways

modulo

10

9

+ 7

.

Return

an integer array

answer

where

answer.length
                == queries.length

, and

answer[i]

is the answer to
                the

i

th

query.

Example 1:

Input:

queries = [[2,6],[5,1],[73,660]]

Output:

[4,1,50734910]

Explanation:

Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 10

9

+ 7 = 50734910.

Example 2:

Input:

queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]

Output:

[1,2,3,10,5]

Constraints:

1 <= queries.length <= 10

4

1 <= n

i

, k

i

<= 10

4

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

Problem Solution

-1735-Count-Ways-to-Make-Array-With-Product

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly
        every week. They are for personal study and research only, and should not be used for
        commercial purposes. Thank you for your cooperation.

