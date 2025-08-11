# 1010. Pairs of Songs With Total Durations Divisible by 60

**Source:** [https://leetcode.ca/all/1010.html](https://leetcode.ca/all/1010.html)

**Companies:** Amazon, Dropbox, Goldman Sachs, Pocket Gems, Visa

## Description

In a list of songs, the

i

-th song has a duration
        of

time[i]

seconds.

Return the number of pairs of songs for which their total duration in seconds is
        divisible by

60

.  Formally, we want the number of indices

i
            < j

with

(time[i] + time[j]) % 60 == 0

.

Example 1:

Input:

[30,20,150,100,40]

Output:

3

Explanation:

Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input:

[60,60,60]

Output:

3

Explanation:

All three pairs have a total duration of 120, which is divisible by 60.

Difficulty:

Easy

Lock:

Normal

Company:

Amazon

Dropbox

Goldman Sachs

Pocket Gems

Visa

Problem Solution

1010-Pairs-of-Songs-With-Total-Durations-Divisible-by-60

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

