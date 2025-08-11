# 656. Coin Path

**Source:** [https://leetcode.ca/all/656.html](https://leetcode.ca/all/656.html)

**Companies:** Google

## Description

Given an array

A

(index starts at

1

) consisting of N integers:
        A

1

, A

2

, ..., A

N

and an integer

B

. The
        integer

B

denotes that from any place (suppose the index is

i

) in
        the array

A

, you can jump to any one of the place in the array

A

indexed

i+1

,

i+2

, …,

i+B

if this place can be
        jumped to. Also, if you step on the index

i

, you have to pay A

i

coins.
        If A

i

is -1, it means you can’t jump to the place indexed

i

in the array.

Now, you start from the place indexed

1

in the array

A

, and your
        aim is to reach the place indexed

N

using the minimum coins. You need to return
        the path of indexes (starting from 1 to N) in the array you should take to get to the place
        indexed

N

using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such
        path.

If it's not possible to reach the place indexed N then you need to return an empty
        array.

Example 1:

Input:

[1,2,4,-1,2], 2

Output:

[1,3,5]

Example 2:

Input:

[1,2,4,-1,2], 1

Output:

[]

Note:

Path Pa

1

, Pa

2

, ..., Pa

n

is lexicographically
            smaller than Pb

1

, Pb

2

, ..., Pb

m

, if and only if at the
            first

i

where Pa

i

and Pb

i

differ,
            Pa

i

< Pb

i

; when no such

i

exists,
            then

n

<

m

.

A

1

>= 0. A

2

, ..., A

N

(if exist) will in the range of
            [-1, 100].

Length of A is in the range of [1, 1000].

B is in the range of [1, 100].

Difficulty:

Hard

Lock:

Prime

Company:

Google

Problem Solution

656-Coin-Path

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

