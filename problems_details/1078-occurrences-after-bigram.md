# 1078. Occurrences After Bigram

**Source:** [https://leetcode.ca/all/1078.html](https://leetcode.ca/all/1078.html)

**Companies:** Google

## Description

Given words

first

and

second

, consider occurrences in
        some

text

of the form "

first second third

", where

second

comes immediately after

first

, and

third

comes
        immediately after

second

.

For each such occurrence, add "

third

" to the answer, and return the
        answer.

Example 1:

Input:

text =

"alice is a good girl she is a good student"

, first =

"a"

, second =

"good"

Output:

["girl","student"]

Example 2:

Input:

text =

"we will we will rock you"

, first =

"we"

, second =

"will"

Output:

["we","rock"]

Note:

1 <= text.length <= 1000

text

consists of space separated words, where each word consists of
                lowercase English letters.

1 <= first.length, second.length <= 10

first

and

second

consist of lowercase English letters.

Difficulty:

Easy

Lock:

Normal

Company:

Google

Problem Solution

1078-Occurrences-After-Bigram

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

