# 1851. Minimum Interval to Include Each Query

**Source:** [https://leetcode.ca/all/1851.html](https://leetcode.ca/all/1851.html)

**Companies:** Google

## Description

You are given a 2D integer array

intervals

, where

intervals[i] = [left

i

, right

i

]

describes the

i

th

interval starting at

left

i

and ending at

right

i

(inclusive)

. The

size

of an interval is defined as the number of integers it contains, or more formally

right

i

- left

i

+ 1

.

You are also given an integer array

queries

. The answer to the

j

th

query is the

size of the smallest interval

i

such that

left

i

<= queries[j] <= right

i

. If no such interval exists, the answer is

-1

.

Return

an array containing the answers to the queries

.

Example 1:

Input:

intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]

Output:

[3,3,1,4]

Explanation:

The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

Example 2:

Input:

intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]

Output:

[2,-1,4,6]

Explanation:

The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.

Constraints:

1 <= intervals.length <= 10

5

1 <= queries.length <= 10

5

intervals[i].length == 2

1 <= left

i

<= right

i

<= 10

7

1 <= queries[j] <= 10

7

Difficulty:

Hard

Lock:

Normal

Company:

Google

Problem Solution

Leetcode Solutions Java Python C++

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

