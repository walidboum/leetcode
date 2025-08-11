# 1763. Longest Nice Substring

**Source:** [https://leetcode.ca/all/1763.html](https://leetcode.ca/all/1763.html)

**Companies:** Microsoft

## Description

A string

s

is

nice

if, for every letter of the alphabet that

s

contains, it appears

both

in uppercase and lowercase. For example,

"abABB"

is nice because

'A'

and

'a'

appear, and

'B'

and

'b'

appear. However,

"abA"

is not because

'b'

appears, but

'B'

does not.

Given a string

s

, return

the longest

substring

of

s

that is

nice

. If there are multiple, return the substring of the

earliest

occurrence. If there are none, return an empty string

.

Example 1:

Input:

s = "YazaAay"

Output:

"aAa"

Explanation:

"aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:

Input:

s = "Bb"

Output:

"Bb"

Explanation:

"Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:

Input:

s = "c"

Output:

""

Explanation:

There are no nice substrings.

Example 4:

Input:

s = "dDzeE"

Output:

"dD"

Explanation:

Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.

Constraints:

1 <= s.length <= 100

s

consists of uppercase and lowercase English letters.

Difficulty:

Easy

Lock:

Normal

Company:

Microsoft

Problem Solution

1763-Longest-Nice-Substring

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

