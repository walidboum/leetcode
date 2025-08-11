# 1613. Find the Missing IDs

**Source:** [https://leetcode.ca/all/1613.html](https://leetcode.ca/all/1613.html)

**Companies:** Amazon

## Description

SQL Schema

Table:

Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the primary key for this table.
Each row of this table contains the name and the id customer.

Write an SQL query to find the missing customer IDs. The missing IDs are ones that
                are not in the

Customers

table but are in the range between

1

and the

maximum

customer_id

present in
                the table.

Notice

that the maximum

customer_id

will not exceed

100

.

Return the result table ordered by

ids

in

ascending
                order

.

The query result format is in the following example.

Customer

table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+

Result table:
+-----+
|

ids

|
+-----+
| 2   |
| 3   |
+-----+
The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.

Difficulty:

Medium

Lock:

Prime

Company:

Amazon

Problem Solution

1613-Find-the-Missing-IDs

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

