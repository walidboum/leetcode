# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters

**Source:** [https://leetcode.ca/all/1576.html](https://leetcode.ca/all/1576.html)

**Companies:** Microsoft

## Description

Given a string

s

containing only lower case
            English letters and the '?' character, convert

all

the '?'
            characters into lower case letters such that the final string does not contain any

consecutive repeating

characters. You

cannot

modify the non '?' characters.

It is

guaranteed

that there are no consecutive repeating characters
                in the given string

except

for '?'.

Return the final string after all the conversions (possibly zero) have been made. If
                there is more than one solution, return any of them. It can be shown that an
                answer is always possible with the given constraints.

Example 1:

Input:

s = "?zs"

Output:

"azs"

Explanation

: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

Example 2:

Input:

s = "ubv?w"

Output:

"ubvaw"

Explanation

: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

Example 3:

Input:

s = "j?qg??b"

Output:

"jaqgacb"

Example 4:

Input:

s = "??yw?ipkj?"

Output:

"acywaipkja"

Constraints:

1 <= s.length <= 100

s

contains only lower case English letters and '?'.

Difficulty:

Easy

Lock:

Normal

Company:

Microsoft

Problem Solution

1576-Replace-All-'s-to-Avoid-Consecutive-Repeating-Characters-

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

