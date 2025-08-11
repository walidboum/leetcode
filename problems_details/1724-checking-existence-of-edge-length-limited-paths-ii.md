# 1724. Checking Existence of Edge Length Limited Paths II

**Source:** [https://leetcode.ca/all/1724.html](https://leetcode.ca/all/1724.html)

**Companies:** Google

## Description

An undirected graph of

n

nodes is defined by

edgeList

,
            where

edgeList[i] = [u

i

, v

i

, dis

i

]

denotes
            an edge between nodes

u

i

and

v

i

with
            distance

dis

i

. Note that there may be

multiple

edges between two nodes, and the graph may not be connected.

Implement the

DistanceLimitedPathsExist

class:

DistanceLimitedPathsExist(int n, int[][] edgeList)

Initializes the
                    class with an undirected graph.

boolean query(int p, int q, int limit)

Returns

true

if
                    there exists a path from

p

to

q

such that each edge on
                    the path has a distance

strictly less than

limit

,
                    and otherwise

false

.

Example 1:

Input

["DistanceLimitedPathsExist", "query", "query", "query", "query"]
[[6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]], [2, 3, 2], [1, 3, 3], [2, 0, 3], [0, 5, 6]]

Output

[null, true, false, true, false]

Explanation

DistanceLimitedPathsExist distanceLimitedPathsExist = new DistanceLimitedPathsExist(6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]);
distanceLimitedPathsExist.query(2, 3, 2); // return true. There is an edge from 2 to 3 of distance 1, which is less than 2.
distanceLimitedPathsExist.query(1, 3, 3); // return false. There is no way to go from 1 to 3 with distances

strictly

less than 3.
distanceLimitedPathsExist.query(2, 0, 3); // return true. There is a way to go from 2 to 0 with distance < 3: travel from 2 to 3 to 0.
distanceLimitedPathsExist.query(0, 5, 6); // return false. There are no paths from 0 to 5.

Constraints:

2 <= n <= 10

4

0 <= edgeList.length <= 10

4

edgeList[i].length == 3

0 <= u

i

, v

i

, p, q <= n-1

u

i

!= v

i

p != q

1 <= dis

i

, limit <= 10

9

At most

10

4

calls will be made to

query

.

Difficulty:

Hard

Lock:

Prime

Company:

Google

Problem Solution

-1724-Checking-Existence-of-Edge-Length-Limited-Paths-II

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly
        every week. They are for personal study and research only, and should not be used for
        commercial purposes. Thank you for your cooperation.

