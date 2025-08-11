# 632. Smallest Range Covering Elements from K Lists

**Source:** [https://leetcode.ca/all/632.html](https://leetcode.ca/all/632.html)

**Companies:** Amazon, Facebook, Google, Lyft, Microsoft, Pinterest, Snapchat

## Description

You have

k

lists of sorted integers in ascending order. Find the

smallest

range that includes at least one number from each of the

k

lists.

We define the range [a,b] is smaller than range [c,d] if

b-a < d-c

or

a
        < c

if

b-a == d-c

.

Example 1:

Input:

[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

Output:

[20,24]

Explanation:

List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Note:

The given list may contain duplicates, so ascending order means >= here.

1 <=

k

<= 3500

-10

5

<=

value of elements

<= 10

5

.

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

Facebook

Google

Lyft

Microsoft

Pinterest

Snapchat

Problem Solution

632-Smallest-Range-Covering-Elements-from-K-Lists

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

