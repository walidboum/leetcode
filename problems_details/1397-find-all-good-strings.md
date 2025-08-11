# 1397. Find All Good Strings

**Source:** [https://leetcode.ca/all/1397.html](https://leetcode.ca/all/1397.html)

**Companies:** dunzo

## Description

Given the strings

s1

and

s2

of size

n

, and
            the string

evil

.

Return the number of

good

strings

.

A

good

string has size

n

, it is alphabetically greater
                than or equal to

s1

, it is alphabetically smaller than or equal to

s2

, and it does not contain the string

evil

as a
                substring. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input:

n = 2, s1 = "aa", s2 = "da", evil = "b"

Output:

51

Explanation:

There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da".

Example 2:

Input:

n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"

Output:

0

Explanation:

All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.

Example 3:

Input:

n = 2, s1 = "gx", s2 = "gz", evil = "x"

Output:

2

Constraints:

s1.length == n

s2.length == n

1 <= n <= 500

1 <= evil.length <= 50

All strings consist of lowercase English letters.

Difficulty:

Hard

Lock:

Normal

Company:

dunzo

Problem Solution

1397-Find-All-Good-Strings

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

