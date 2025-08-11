# 1045. Customers Who Bought All Products

**Source:** [https://leetcode.ca/all/1045.html](https://leetcode.ca/all/1045.html)

**Companies:** Amazon

## Description

Table:

Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
product_key is a foreign key to

Product

table.

Table:

Product

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key column for this table.

Write an SQL query for a report that provides the customer ids from
        the

Customer

table that bought all the products in the

Product

table.

For example:

Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+

Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+

Result table:
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
The customers who bought all the products (5 and 6) are customers with id 1 and 3.

Difficulty:

Medium

Lock:

Prime

Company:

Amazon

Problem Solution

1045-Customers-Who-Bought-All-Products

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

