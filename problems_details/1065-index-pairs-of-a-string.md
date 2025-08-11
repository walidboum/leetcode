# 1065. Index Pairs of a String

**Source:** [https://leetcode.ca/all/1065.html](https://leetcode.ca/all/1065.html)

**Companies:** Amazon

## Description

Given a

text

string and

words

(a list of strings), return all
        index pairs

[i, j]

so that the substring

text[i]...text[j]

is
        in the list of

words

.

Example 1:

Input:

text =

"thestoryofleetcodeandme"

, words =

["story","fleet","leetcode"]

Output:

[[3,7],[9,13],[10,17]]

Example 2:

Input:

text =

"ababa"

, words =

["aba","ab"]

Output:

[[0,1],[0,2],[2,3],[2,4]]

Explanation:

Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

Note:

All strings contains only lowercase English letters.

It's guaranteed that all strings in

words

are different.

1 <= text.length <= 100

1 <= words.length <= 20

1 <= words[i].length <= 50

Return the pairs

[i,j]

in sorted order (i.e. sort them by their first
            coordinate in case of ties sort them by their second coordinate).

Difficulty:

Easy

Lock:

Prime

Company:

Amazon

Problem Solution

1065-Index-Pairs-of-a-String

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

