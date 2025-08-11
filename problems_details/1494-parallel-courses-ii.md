# 1494. Parallel Courses II

**Source:** [https://leetcode.ca/all/1494.html](https://leetcode.ca/all/1494.html)

**Companies:** Google

## Description

Given the integer

n

representing the number of courses at some
            university labeled from

1

to

n

, and the array

dependencies

where

dependencies[i] = [x

i

, y

i

]

represents a
            prerequisite relationship, that is, the course

x

i

must be
            taken before the course

y

i

.  Also, you are given the integer

k

.

In one semester you can take

at most

k

courses as long
                as you have taken all the prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses

. It is
                guaranteed that you can take all courses in some way.

Example 1:

Input:

n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2

Output:

3

Explanation:

The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.

Example 2:

Input:

n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2

Output:

4

Explanation:

The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.

Example 3:

Input:

n = 11, dependencies = [], k = 2

Output:

6

Constraints:

1 <= n <= 15

1 <= k <= n

0 <= dependencies.length <= n * (n-1) / 2

dependencies[i].length == 2

1 <= x

i

, y

i

<= n

x

i

!= y

i

All prerequisite relationships are distinct, that is,

dependencies[i] !=
                    dependencies[j]

.

The given graph is a directed acyclic graph.

Difficulty:

Hard

Lock:

Normal

Company:

Google

Problem Solution

1494-Parallel-Courses-II

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

