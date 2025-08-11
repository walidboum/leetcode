# 1584. Min Cost to Connect All Points

**Source:** [https://leetcode.ca/all/1584.html](https://leetcode.ca/all/1584.html)

**Companies:** Directi

## Description

You are given an array

points

representing integer
            coordinates of some points on a 2D-plane, where

points[i] = [x

i

, y

i

]

.

The cost of connecting two points

[x

i

, y

i

]

and

[x

j

, y

j

]

is the

manhattan
                    distance

between them:

|x

i

- x

j

| +
                    |y

i

- y

j

|

, where

|val|

denotes the
                absolute value of

val

.

Return

the minimum cost to make all points connected.

All points are
                connected if there is

exactly one

simple path between any two
                points.

Example 1:

Input:

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

Output:

20

Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input:

points = [[3,12],[-2,5],[-4,1]]

Output:

18

Example 3:

Input:

points = [[0,0],[1,1],[1,0],[-1,1]]

Output:

4

Example 4:

Input:

points = [[-1000000,-1000000],[1000000,1000000]]

Output:

4000000

Example 5:

Input:

points = [[0,0]]

Output:

0

Constraints:

1 <= points.length <= 1000

-10

6

<= x

i

, y

i

<=
                    10

6

All pairs

(x

i

, y

i

)

are distinct.

Difficulty:

Medium

Lock:

Normal

Company:

Directi

Problem Solution

1584-Min-Cost-to-Connect-All-Points

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

