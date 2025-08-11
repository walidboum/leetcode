# 601. Human Traffic of Stadium

**Source:** [https://leetcode.ca/all/601.html](https://leetcode.ca/all/601.html)

**Companies:** Adobe, Uber

## Description

X city built a new stadium, each day many people visit it and the stats are saved as these
        columns:

id

,

visit_

date

,

people

Please write a query to display the records which have 3 or more consecutive rows and the
        amount of people more than 100(inclusive).

For example, the table

stadium

:

+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+

For the sample data above, the output is:

+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+

Note:

Each day only have one row record, and the dates are increasing with id increasing.

Difficulty:

Hard

Lock:

Normal

Company:

Adobe

Uber

Problem Solution

601-Human-Traffic-of-Stadium

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

