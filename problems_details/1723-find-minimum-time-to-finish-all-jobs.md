# 1723. Find Minimum Time to Finish All Jobs

**Source:** [https://leetcode.ca/all/1723.html](https://leetcode.ca/all/1723.html)

**Companies:** Amazon

## Description

You are given an integer array

jobs

, where

jobs[i]

is the
            amount of time it takes to complete the

i

th

job.

There are

k

workers that you can assign jobs to. Each job should be
                assigned to

exactly

one worker. The

working time

of a worker is the sum of the time it takes to complete all jobs assigned to them.
                Your goal is to devise an optimal assignment such that the

maximum working
                    time

of any worker is

minimized

.

Return the

minimum

possible

maximum working
                time

of any assignment.

Example 1:

Input:

jobs = [3,2,3], k = 3

Output:

3

Explanation:

By assigning each person one job, the maximum time is 3.

Example 2:

Input:

jobs = [1,2,4,7,8], k = 2

Output:

11

Explanation:

Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.

Constraints:

1 <= k <= jobs.length <= 12

1 <= jobs[i] <= 10

7

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

Problem Solution

-1723-Find-Minimum-Time-to-Finish-All-Jobs

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly
        every week. They are for personal study and research only, and should not be used for
        commercial purposes. Thank you for your cooperation.

