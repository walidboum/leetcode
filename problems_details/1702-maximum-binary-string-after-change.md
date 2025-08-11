# 1702. Maximum Binary String After Change

**Source:** [https://leetcode.ca/all/1702.html](https://leetcode.ca/all/1702.html)

**Companies:** Huawei

## Description

You are given a binary string

binary

consisting of only

0

's
            or

1

's. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring

"00"

, you can
                    replace it with

"10"

.

For example,

"

00

010" -> "

10

010

"

Operation 2: If the number contains the substring

"10"

, you can
                    replace it with

"01"

.

For example,

"000

10

" -> "000

01

"

Return the

maximum binary string

you can obtain after any number
                of operations. Binary string

x

is greater than binary string

y

if

x

's decimal representation is greater than

y

's decimal representation.

Example 1:

Input:

binary = "000110"

Output:

"111011"

Explanation:

A valid transformation sequence can be:
"0001

10

" -> "0001

01

"
"

00

0101" -> "

10

0101"
"1

00

101" -> "1

10

101"
"110

10

1" -> "110

01

1"
"11

00

11" -> "11

10

11"

Example 2:

Input:

binary = "01"

Output:

"01"

Explanation:

"01" cannot be transformed any further.

Constraints:

1 <= binary.length <= 10

5

binary

consist of

'0'

and

'1'

.

Difficulty:

Medium

Lock:

Normal

Company:

Huawei

Problem Solution

1702-Maximum-Binary-String-After-Change

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

