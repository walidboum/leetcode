# 1527. Patients With a Condition

**Source:** [https://leetcode.ca/all/1527.html](https://leetcode.ca/all/1527.html)

**Companies:** Unknown

## Description

SQL Schema

Table:

Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key for this table.
'conditions' contains 0 or more code separated by spaces.
This table contains information of the patients in the hospital.

Write an SQL query to report the patient_id, patient_name all conditions of patients
                who have Type I Diabetes. Type I Diabetes always starts with

DIAB1

prefix

Return the result table in any order.

The query result format is in the following example.

Patients

+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+

Result table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
+------------+--------------+--------------+
Bob and George both have a condition that starts with DIAB1.

Difficulty:

Easy

Lock:

Prime

Company:

Unknown

Problem Solution

1527-Patients-With-a-Condition

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

