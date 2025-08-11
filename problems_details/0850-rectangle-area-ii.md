# 850. Rectangle Area II

**Source:** [https://leetcode.ca/all/850.html](https://leetcode.ca/all/850.html)

**Companies:** Google, Sumologic

## Description

We are given a list of (axis-aligned)

rectangles

.  Each

rectangle[i]
        = [x1, y1, x2, y2]

, where (x1, y1) are the coordinates of the bottom-left
        corner, and (x2, y2) are the coordinates of the top-right corner of the

i

th
        rectangle.

Find the total area covered by all

rectangles

in the plane.  Since the
        answer may be too large,

return it modulo 10^9 + 7

.

Example 1:

Input:

[[0,0,2,2],[1,0,2,3],[1,0,3,1]]

Output:

6

Explanation:

As illustrated in the picture.

Example 2:

Input:

[[0,0,1000000000,1000000000]]

Output:

49

Explanation:

The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.

Note:

1 <= rectangles.length <= 200

rectanges[i].length = 4

0 <= rectangles[i][j] <= 10^9

The total area covered by all rectangles will never exceed

2^63 - 1

and
            thus will fit in a 64-bit signed integer.

Difficulty:

Hard

Lock:

Normal

Company:

Google

Sumologic

Problem Solution

850-Rectangle-Area-II

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

