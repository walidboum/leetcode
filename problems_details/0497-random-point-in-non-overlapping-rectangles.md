# 497. Random Point in Non-overlapping Rectangles

**Source:** [https://leetcode.ca/all/497.html](https://leetcode.ca/all/497.html)

**Companies:** Google

## Description

Given a list of

non-overlapping

axis-aligned rectangles

rects

, write a function

pick

which randomly and uniformily picks
        an

integer point

in the space covered by the rectangles.

Note:

An

integer point

is a point that has integer coordinates.

A point on the perimeter of a rectangle is

included

in
            the space covered by the rectangles.

i

th rectangle =

rects[i]

=

[x1,y1,x2,y2]

,
            where

[x1, y1]

are the integer coordinates of the bottom-left corner,
            and

[x2, y2]

are the integer coordinates of the top-right corner.

length and width of each rectangle does not exceed

2000

.

1 <= rects.length <= 100

pick

return a point as an array of integer coordinates

[p_x,
            p_y]

pick

is called at most

10000

times.

Example 1:

Input:

["Solution","pick","pick","pick"]

[[[[1,1,5,5]]],[],[],[]]

Output:

[null,[4,1],[4,1],[3,3]]

Example 2:

Input:

["Solution","pick","pick","pick","pick","pick"]

[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]

Output:

[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

Difficulty:

Medium

Lock:

Normal

Company:

Google

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

