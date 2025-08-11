# 1585. Check If String Is Transformable With Substring Sort Operations

**Source:** [https://leetcode.ca/all/1585.html](https://leetcode.ca/all/1585.html)

**Companies:** Google

## Description

Given two strings

s

and

t

, you want to transform
            string

s

into string

t

using the following operation
            any number of times:

Choose a

non-empty

substring in

s

and
                    sort it in-place so the characters are in

ascending
                        order

.

For example, applying the operation on the underlined substring in

"1

4234

"

results
                in

"1

2344

"

.

Return

true

if

it is possible to transform string

s

into
                string

t

. Otherwise, return

false

.

A

substring

is a contiguous sequence of characters within a
                string.

Example 1:

Input:

s = "84532", t = "34852"

Output:

true

Explanation:

You can transform s into t using the following sort operations:
"84

53

2" (from index 2 to 3) -> "84

35

2"
"

843

52" (from index 0 to 2) -> "

348

52"

Example 2:

Input:

s = "34521", t = "23415"

Output:

true

Explanation:

You can transform s into t using the following sort operations:
"

3452

1" -> "

2345

1"
"234

51

" -> "234

15

"

Example 3:

Input:

s = "12345", t = "12435"

Output:

false

Example 4:

Input:

s = "1", t = "2"

Output:

false

Constraints:

s.length == t.length

1 <= s.length <= 10

5

s

and

t

only contain digits from

'0'

to

'9'

.

Difficulty:

Hard

Lock:

Normal

Company:

Google

Problem Solution

1585-Check-If-String-Is-Transformable-With-Substring-Sort-Operations

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

