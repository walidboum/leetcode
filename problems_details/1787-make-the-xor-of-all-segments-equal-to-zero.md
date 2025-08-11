# 1787. Make the XOR of All Segments Equal to Zero

**Source:** [https://leetcode.ca/all/1787.html](https://leetcode.ca/all/1787.html)

**Companies:** Unknown

## Description

You are given an array

nums

âââ and an integer

k

âââââ. The

XOR

of a segment

[left, right]

where

left <= right

is the

XOR

of all the elements with indices between

left

and

right

, inclusive:

nums[left] XOR nums[left+1] XOR ... XOR nums[right]

.

Return

the minimum number of elements to change in the array

such that the

XOR

of all segments of size

k

ââââââ is equal to zero.

Example 1:

Input:

nums = [1,2,0,3,0], k = 1

Output:

3

Explanation:

Modify the array from [

1

,

2

,0,

3

,0] to from [

0

,

0

,0,

0

,0].

Example 2:

Input:

nums = [3,4,5,2,1,7,3,4,7], k = 3

Output:

3

Explanation:

Modify the array from [3,4,

5

,

2

,

1

,7,3,4,7] to [3,4,

7

,

3

,

4

,7,3,4,7].

Example 3:

Input:

nums = [1,2,4,1,2,5,1,2,6], k = 3

Output:

3

Explanation:

Modify the array from [1,2,

4,

1,2,

5

,1,2,

6

] to [1,2,

3

,1,2,

3

,1,2,

3

].

Constraints:

1 <= k <= nums.length <= 2000

ââââââ0 <= nums[i] < 2

10

Difficulty:

Hard

Lock:

Normal

Company:

Unknown

Problem Solution

1787-Make-the-XOR-of-All-Segments-Equal-to-Zero

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

