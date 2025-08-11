# 1734. Decode XORed Permutation

**Source:** [https://leetcode.ca/all/1734.html](https://leetcode.ca/all/1734.html)

**Companies:** Amazon

## Description

There is an integer array

perm

that is a permutation of the first

n

positive integers, where

n

is always

odd

.

It was encoded into another integer array

encoded

of length

n -
                1

, such that

encoded[i] = perm[i] XOR perm[i + 1]

. For example,
                if

perm = [1,3,2]

, then

encoded = [2,1]

.

Given the

encoded

array, return

the original array

perm

. It is guaranteed that the answer exists and is unique.

Example 1:

Input:

encoded = [3,1]

Output:

[1,2,3]

Explanation:

If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

Example 2:

Input:

encoded = [6,5,4,6]

Output:

[2,4,1,5,3]

Constraints:

3 <= n < 10

5

n

is odd.

encoded.length == n - 1

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Problem Solution

-1734-Decode-XORed-Permutation

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly
        every week. They are for personal study and research only, and should not be used for
        commercial purposes. Thank you for your cooperation.

