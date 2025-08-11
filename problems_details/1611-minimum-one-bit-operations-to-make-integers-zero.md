# 1611. Minimum One Bit Operations to Make Integers Zero

**Source:** [https://leetcode.ca/all/1611.html](https://leetcode.ca/all/1611.html)

**Companies:** Expedia

## Description

Given an integer

n

, you must transform it into

0

using the
            following operations any number of times:

Change the rightmost (

0

th

) bit in the binary
                    representation of

n

.

Change the

i

th

bit in the binary representation of

n

if the

(i-1)

th

bit is set to

1

and the

(i-2)

th

through

0

th

bits are set to

0

.

Return

the minimum number of operations to transform

n

into

0

.

Example 1:

Input:

n = 0

Output:

0

Example 2:

Input:

n = 3

Output:

2

Explanation:

The binary representation of 3 is "11".
"

1

1" -> "

0

1" with the 2nd operation since the 0th bit is 1.
"0

1

" -> "0

0

" with the 1st operation.

Example 3:

Input:

n = 6

Output:

4

Explanation:

The binary representation of 6 is "110".
"

1

10" -> "

0

10" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"01

0

" -> "01

1

" with the 1st operation.
"0

1

1" -> "0

0

1" with the 2nd operation since the 0th bit is 1.
"00

1

" -> "00

0

" with the 1st operation.

Example 4:

Input:

n = 9

Output:

14

Example 5:

Input:

n = 333

Output:

393

Constraints:

0 <= n <= 10

9

Difficulty:

Hard

Lock:

Normal

Company:

Expedia

Problem Solution

1611-Minimum-One-Bit-Operations-to-Make-Integers-Zero

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

