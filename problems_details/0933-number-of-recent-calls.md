# 933. Number of Recent Calls

**Source:** [https://leetcode.ca/all/933.html](https://leetcode.ca/all/933.html)

**Companies:** Bloomberg, Google

## Description

Write a class

RecentCounter

to count recent requests.

It has only one method:

ping(int t)

, where t represents some time in
        milliseconds.

Return the number of

ping

s that have been made from 3000 milliseconds ago until
        now.

Any ping with time in

[t - 3000, t]

will count, including the current ping.

It is guaranteed that every call to

ping

uses a strictly larger value
        of

t

than before.

Example 1:

Input:

inputs =

["RecentCounter","ping","ping","ping","ping"]

, inputs =

[[],[1],[100],[3001],[3002]]

Output:

[null,1,2,3,3]

Note:

Each test case will have at most

10000

calls to

ping

.

Each test case will call

ping

with strictly increasing values of

t

.

Each call to ping will have

1 <= t <= 10^9

.

Difficulty:

Easy

Lock:

Normal

Company:

Bloomberg

Google

Problem Solution

933-Number-of-Recent-Calls

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

