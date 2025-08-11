# 874. Walking Robot Simulation

**Source:** [https://leetcode.ca/all/874.html](https://leetcode.ca/all/874.html)

**Companies:** Jane Street

## Description

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can
        receive one of three possible types of commands:

-2

: turn left 90 degrees

-1

: turn right 90 degrees

1 <= x <= 9

: move forward

x

units

Some of the grid squares are obstacles.

The

i

-th obstacle is at grid point

(obstacles[i][0],
        obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead
        (but still continues following the rest of the route.)

Return the

square

of the maximum Euclidean distance that the robot will be
        from the origin.

Example 1:

Input:

commands =

[4,-1,3]

, obstacles =

[]

Output:

25

Explanation:

robot will go to (3, 4)

Example 2:

Input:

commands =

[4,-1,4,-2,4]

, obstacles =

[[2,4]]

Output:

65

Explanation

: robot will be stuck at (1, 4) before turning left and going to (1, 8)

Difficulty:

Easy

Lock:

Normal

Company:

Jane Street

Problem Solution

874-Walking-Robot-Simulation

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

