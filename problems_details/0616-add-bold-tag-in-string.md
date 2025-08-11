# 616. Add Bold Tag in String

**Source:** [https://leetcode.ca/all/616.html](https://leetcode.ca/all/616.html)

**Companies:** Facebook, Google

## Description

Given a string

s

and a list of strings

dict

, you need to add a closed pair of bold
    tag

<b>

and

</b>

to wrap the substrings in s that exist in
    dict. If two such substrings overlap, you need to wrap them together by only one pair of closed
    bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine
    them.

Example 1:

Input:

s = "abcxyz123"
dict = ["abc","123"]

Output:

"<b>abc</b>xyz<b>123</b>"

Example 2:

Input:

s = "aaabbcc"
dict = ["aaa","aab","bc"]

Output:

"<b>aaabbc</b>c"

Note:

The given dict won't contain duplicates, and its length won't exceed 100.

All the strings in input have length in range [1, 1000].

Difficulty:

Medium

Lock:

Prime

Company:

Facebook

Google

Problem Solution

616-Add-Bold-Tag-in-String

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

