# 1408. String Matching in an Array

**Source:** [https://leetcode.ca/all/1408.html](https://leetcode.ca/all/1408.html)

**Companies:** Amazon

## Description

Given an array of string

words

. Return all strings in

words

which is substring of another word in

any

order.

String

words[i]

is substring of

words[j]

, if can
                be obtained removing some characters to left and/or right side of

words[j]

.

Example 1:

Input:

words = ["mass","as","hero","superhero"]

Output:

["as","hero"]

Explanation:

"as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input:

words = ["leetcode","et","code"]

Output:

["et","code"]

Explanation:

"et", "code" are substring of "leetcode".

Example 3:

Input:

words = ["blue","green","bu"]

Output:

[]

Constraints:

1 <= words.length <= 100

1 <= words[i].length <= 30

words[i]

contains only lowercase English letters.

It's

guaranteed

that

words[i]

will be
                    unique.

Difficulty:

Easy

Lock:

Normal

Company:

Amazon

Problem Solution

1408-String-Matching-in-an-Array

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

