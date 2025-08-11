# 1285. Find the Start and End Number of Continuous Ranges

**Source:** [https://leetcode.ca/all/1285.html](https://leetcode.ca/all/1285.html)

**Companies:** Microsoft, Unknown

## Description

SQL Schema

Table:

Logs

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| log_id        | int     |
+---------------+---------+
id is the primary key for this table.
Each row of this table contains the ID in a log Table.

Since some IDs have been removed from

Logs

. Write an SQL query to
                find the start and end number of continuous ranges in table

Logs

.

Order the result table by

start_id

.

The query result format is in the following example:

Logs table:
+------------+
| log_id     |
+------------+
| 1          |
| 2          |
| 3          |
| 7          |
| 8          |
| 10         |
+------------+

Result table:
+------------+--------------+
| start_id   | end_id       |
+------------+--------------+
| 1          | 3            |
| 7          | 8            |
| 10         | 10           |
+------------+--------------+
The result table should contain all ranges in table Logs.
From 1 to 3 is contained in the table.
From 4 to 6 is missing in the table
From 7 to 8 is contained in the table.
Number 9 is missing in the table.
Number 10 is contained in the table.

Difficulty:

Medium

Lock:

Prime

Company:

Microsoft

Unknown

Problem Solution

1285-Find-the-Start-and-End-Number-of-Continuous-Ranges

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

