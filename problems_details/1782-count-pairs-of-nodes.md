# 1782. Count Pairs Of Nodes

**Source:** [https://leetcode.ca/all/1782.html](https://leetcode.ca/all/1782.html)

**Companies:** Amazon

## Description

You are given an undirected graph represented by an integer

n

, which is the number of nodes, and

edges

, where

edges[i] = [u

i

, v

i

]

which indicates that there is an undirected edge between

u

i

and

v

i

. You are also given an integer array

queries

.

The answer to the

j

th

query is the number of pairs of nodes

(a, b)

that satisfy the following conditions:

a < b

cnt

is

strictly greater

than

queries[j]

, where

cnt

is the number of edges incident to

a

or

b

.

Return an array

answers

such that

answers.length == queries.length

and

answers[j]

is the answer of the

j

th

query.

Note that there can be

repeated edges

.

Example 1:

Input:

n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]

Output:

[6,5]

Explanation:

The number of edges incident to at least one of each pair is shown above.

Example 2:

Input:

n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]

Output:

[10,10,9,8,6]

Constraints:

2 <= n <= 2 * 10

4

1 <= edges.length <= 10

5

1 <= u

i

, v

i

<= n

u

i

!= v

i

1 <= queries.length <= 20

0 <= queries[j] < edges.length

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

Problem Solution

1782-Count-Pairs-Of-Nodes

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

