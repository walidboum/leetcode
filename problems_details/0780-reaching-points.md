# 780. Reaching Points

**Source:** [https://leetcode.ca/all/780.html](https://leetcode.ca/all/780.html)

**Companies:** Coursera, Google, Quora, Salesforce, Twitter, Uber

## Description

A move consists of taking a point

(x, y)

and transforming it to either

(x,
        x+y)

or

(x+y, y)

.

Given a starting point

(sx, sy)

and a target point

(tx, ty)

, return

True

if and only if a sequence of moves exists to transform the point

(sx,
            sy)

to

(tx, ty)

. Otherwise, return

False

.

Examples:

Input:

sx = 1, sy = 1, tx = 3, ty = 5

Output:

True

Explanation:

One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input:

sx = 1, sy = 1, tx = 2, ty = 2

Output:

False

Input:

sx = 1, sy = 1, tx = 1, ty = 1

Output:

True

Note:

sx, sy, tx, ty

will all be integers in the range

[1, 10^9]

.

Difficulty:

Hard

Lock:

Normal

Company:

Coursera

Google

Quora

Salesforce

Twitter

Uber

Problem Solution

780-Reaching-Points

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

