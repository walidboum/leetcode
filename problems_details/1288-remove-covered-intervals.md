# 1288. Remove Covered Intervals

**Source:** [https://leetcode.ca/all/1288.html](https://leetcode.ca/all/1288.html)

**Companies:** Amazon

## Description

Given a list of intervals, remove all intervals that are covered by another interval
            in the list. Interval

[a,b)

is covered by interval

[c,d)

if and only if

c <= a

and

b <= d

.

After doing so, return the number of remaining intervals.

Example 1:

Input:

intervals = [[1,4],[3,6],[2,8]]

Output:

2

Explanation:

Interval [3,6] is covered by [2,8], therefore it is removed.

Constraints:

1 <= intervals.length <= 1000

0 <= intervals[i][0] < intervals[i][1] <= 10^5

intervals[i] != intervals[j]

for all

i != j

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Problem Solution

1288-Remove-Covered-Intervals

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

