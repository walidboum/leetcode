# 745. Prefix and Suffix Search

**Source:** [https://leetcode.ca/all/745.html](https://leetcode.ca/all/745.html)

**Companies:** Facebook, Google, Uber

## Description

Given many

words

,

words[i]

has weight

i

.

Design a class

WordFilter

that supports one function,

WordFilter.f(String
        prefix, String suffix)

. It will return the word with given

prefix

and

suffix

with maximum weight. If no word exists, return -1.

Examples:

Input:

WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1

Note:

words

has length in range

[1, 15000]

.

For each test case, up to

words.length

queries

WordFilter.f

may be made.

words[i]

has length in range

[1, 10]

.

prefix, suffix

have lengths in range

[0, 10]

.

words[i]

and

prefix, suffix

queries consist of lowercase
            letters only.

Difficulty:

Hard

Lock:

Normal

Company:

Facebook

Google

Uber

Problem Solution

745-Prefix-and-Suffix-Search

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

