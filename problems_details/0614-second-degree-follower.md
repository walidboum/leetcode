# 614. Second Degree Follower

**Source:** [https://leetcode.ca/all/614.html](https://leetcode.ca/all/614.html)

**Companies:** Facebook

## Description

In facebook, there is a

follow

table with two columns:

followee

,

follower

.

Please write a sql query to get the amount of each follower’s follower if he/she has
        one.

For example:

+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+

should output:

+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+

Explaination:

Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's
    follower is E. A does not exist in follower list.

Note:

Followee would not follow himself/herself in all cases.

Please display the result in follower's alphabet order.

Difficulty:

Medium

Lock:

Prime

Company:

Facebook

Problem Solution

614-Second-Degree-Follower

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

