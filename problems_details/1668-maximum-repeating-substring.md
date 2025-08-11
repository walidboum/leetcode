# 1668. Maximum Repeating Substring

**Source:** [https://leetcode.ca/all/1668.html](https://leetcode.ca/all/1668.html)

**Companies:** Asana

## Description

For a string

sequence

, a string

word

is

k

-repeating

if

word

concatenated

k

times is a substring of

sequence

. The

word

's

maximum

k

-repeating value

is the highest value

k

where

word

is

k

-repeating in

sequence

. If

word

is not a substring of

sequence

,

word

's maximum

k

-repeating value is

0

.

Given strings

sequence

and

word

, return

the

maximum

k

-repeating value

of

word

in

sequence

.

Example 1:

Input:

sequence = "ababc", word = "ab"

Output:

2

Explanation:

"abab" is a substring in "

abab

c".

Example 2:

Input:

sequence = "ababc", word = "ba"

Output:

1

Explanation:

"ba" is a substring in "a

ba

bc". "baba" is not a substring in "ababc".

Example 3:

Input:

sequence = "ababc", word = "ac"

Output:

0

Explanation:

"ac" is not a substring in "ababc".

Constraints:

1 <= sequence.length <= 100

1 <= word.length <= 100

sequence

and

word

contains only lowercase English
                    letters.

Difficulty:

Easy

Lock:

Normal

Company:

Asana

Problem Solution

1668-Maximum-Repeating-Substring

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

