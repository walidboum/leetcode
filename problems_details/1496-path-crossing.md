# 1496. Path Crossing

**Source:** [https://leetcode.ca/all/1496.html](https://leetcode.ca/all/1496.html)

**Companies:** Amazon

## Description

Given a string

path

, where

path[i] = 'N'

,

'S'

,

'E'

or

'W'

, each representing
            moving one unit north, south, east, or west, respectively. You start at the origin

(0, 0)

on a 2D plane and walk on the path specified by

path

.

Return

True

if the path crosses itself at any point, that is, if at any time
            you are on a location you've previously visited. Return

False

otherwise.

Example 1:

Input:

path = "NES"

Output:

false

Explanation:

Notice that the path doesn't cross any point more than once.

Example 2:

Input:

path = "NESWW"

Output:

true

Explanation:

Notice that the path visits the origin twice.

Constraints:

1 <= path.length <= 10^4

path

will only consist of characters in

{'N', 'S', 'E',
                'W}

Difficulty:

Easy

Lock:

Normal

Company:

Amazon

Problem Solution

1496-Path-Crossing

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

