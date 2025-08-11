# 978. Longest Turbulent Subarray

**Source:** [https://leetcode.ca/all/978.html](https://leetcode.ca/all/978.html)

**Companies:** Amazon, Bloomberg

## Description

A subarray

A[i], A[i+1], ..., A[j]

of

A

is said to be

turbulent

if and only if:

For

i <= k < j

,

A[k] > A[k+1]

when

k

is
            odd, and

A[k] < A[k+1]

when

k

is even;

OR

, for

i <= k < j

,

A[k] > A[k+1]

when

k

is even, and

A[k] < A[k+1]

when

k

is
            odd.

That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of
        elements in the subarray.

Return the

length

of a maximum size turbulent subarray of A.

Example 1:

Input:

[9,4,2,10,7,8,8,1,9]

Output:

5

Explanation:

(A[1] > A[2] < A[3] > A[4] < A[5])

Example 2:

Input:

[4,8,12,16]

Output:

2

Example 3:

Input:

[100]

Output:

1

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Bloomberg

Problem Solution

978-Longest-Turbulent-Subarray

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

