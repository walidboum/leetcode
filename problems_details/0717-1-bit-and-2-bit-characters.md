# 717. 1-bit and 2-bit Characters

**Source:** [https://leetcode.ca/all/717.html](https://leetcode.ca/all/717.html)

**Companies:** Google, IXL, Microsoft, Quora

## Description

We have two special characters. The first character can be represented by one bit

0

. The second character can be represented by two bits (

10

or

11

).

Now given a string represented by several bits. Return whether the last character must be a
        one-bit character or not. The given string will always end with a zero.

Example 1:

Input:

bits = [1, 0, 0]

Output:

True

Explanation:

The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:

Input:

bits = [1, 1, 1, 0]

Output:

False

Explanation:

The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:

1 <= len(bits) <= 1000

.

bits[i]

is always

0

or

1

.

Difficulty:

Easy

Lock:

Normal

Company:

Google

IXL

Microsoft

Quora

Problem Solution

717-1-bit-and-2-bit-Characters

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

