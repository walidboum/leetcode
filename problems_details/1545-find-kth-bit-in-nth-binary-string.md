# 1545. Find Kth Bit in Nth Binary String

**Source:** [https://leetcode.ca/all/1545.html](https://leetcode.ca/all/1545.html)

**Companies:** Rupeek

## Description

Given two positive integers

n

and

k

, the
            binary string

S

n

is formed as follows:

S

1

= "0"

S

i

= S

i-1

+ "1" + reverse(invert(S

i-1

))

for

i
                    > 1

Where

+

denotes the concatenation operation,

reverse(x)

returns
                the reversed string

x,

and

invert(x)

inverts
                all the bits in

x

(0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

S

1

= "0"

S

2

= "0

1

1"

S

3

= "011

1

001"

S

4

= "0111001

1

0110001"

Return

the

k

th

bit

in

S

n

.
                It is guaranteed that

k

is valid for the
                given

n

.

Example 1:

Input:

n = 3, k = 1

Output:

"0"

Explanation:

S

3

is "

0

111001". The first bit is "0".

Example 2:

Input:

n = 4, k = 11

Output:

"1"

Explanation:

S

4

is "0111001101

1

0001". The 11th bit is "1".

Example 3:

Input:

n = 1, k = 1

Output:

"0"

Example 4:

Input:

n = 2, k = 3

Output:

"1"

Constraints:

1 <= n <= 20

1 <= k <= 2

n

- 1

Difficulty:

Medium

Lock:

Normal

Company:

Rupeek

Problem Solution

1545-Find-Kth-Bit-in-Nth-Binary-String

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

