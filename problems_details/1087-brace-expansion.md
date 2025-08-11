# 1087. Brace Expansion

**Source:** [https://leetcode.ca/all/1087.html](https://leetcode.ca/all/1087.html)

**Companies:** Google

## Description

A string

S

represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is
        represented as is.  If there is more than one option, then curly braces delimit the
        options.  For example,

"{a,b,c}"

represents options

["a",
            "b", "c"]

.

For example,

"{a,b,c}d{e,f}"

represents the list

["ade",
        "adf", "bde", "bdf", "cde", "cdf"]

.

Return all words that can be formed in this manner, in lexicographical order.

Example 1:

Input:

"{a,b}c{d,e}f"

Output:

["acdf","acef","bcdf","bcef"]

Example 2:

Input:

"abcd"

Output:

["abcd"]

Note:

1 <= S.length <= 50

There are no nested curly brackets.

All characters inside a pair of consecutive opening and ending curly brackets are
            different.

Difficulty:

Medium

Lock:

Prime

Company:

Google

Problem Solution

1087-Brace-Expansion

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

