# 1041. Robot Bounded In Circle

**Source:** [https://leetcode.ca/all/1041.html](https://leetcode.ca/all/1041.html)

**Companies:** Airbnb, Paypal, Qualtrics, Twitter

## Description

On an infinite plane, a robot initially stands at

(0, 0)

and faces north.  The
        robot can receive one of three instructions:

"G"

: go straight 1 unit;

"L"

: turn 90 degrees to the left;

"R"

: turn 90 degress to the right.

The robot performs the

instructions

given in order, and repeats them forever.

Return

true

if and only if there exists a circle in the plane such that the
        robot never leaves the circle.

Example 1:

Input:

"GGLLGG"

Output:

true

Explanation:

The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input:

"GG"

Output:

false

Explanation:

The robot moves north indefinitely.

Example 3:

Input:

"GL"

Output:

true

Explanation:

The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Note:

1 <= instructions.length <= 100

instructions[i]

is in

{'G', 'L', 'R'}

Difficulty:

Medium

Lock:

Normal

Company:

Airbnb

Paypal

Qualtrics

Twitter

Problem Solution

1041-Robot-Bounded-In-Circle

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

