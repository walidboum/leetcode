# 1683. Invalid Tweets

**Source:** [https://leetcode.ca/all/1683.html](https://leetcode.ca/all/1683.html)

**Companies:** Twitter

## Description

SQL Schema

Table:

Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key for this table.
This table contains all the tweets in a social media app.

Write an SQL query to find the IDs of the invalid tweets. The tweet is invalid if the
                number of characters used in the content of the tweet is

strictly
                    greater

than

15

.

Return the result table

in any order

.

The query result format is in the following example:

Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+

Result table:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.

Difficulty:

Easy

Lock:

Prime

Company:

Twitter

Problem Solution

1683-Invalid-Tweets

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

