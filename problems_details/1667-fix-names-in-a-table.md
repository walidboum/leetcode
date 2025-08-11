# 1667. Fix Names in a Table

**Source:** [https://leetcode.ca/all/1667.html](https://leetcode.ca/all/1667.html)

**Companies:** Unknown

## Description

SQL Schema

Table:

Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

Write an SQL query to fix the names so that only the first character is uppercase and
                the rest are lowercase.

Return the result table ordered by

user_id

.

The query result format is in the following example:

Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+

Result table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+

Difficulty:

Easy

Lock:

Prime

Company:

Unknown

Problem Solution

1667-Fix-Names-in-a-Table

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

