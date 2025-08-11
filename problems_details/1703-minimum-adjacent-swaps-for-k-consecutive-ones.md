# 1703. Minimum Adjacent Swaps for K Consecutive Ones

**Source:** [https://leetcode.ca/all/1703.html](https://leetcode.ca/all/1703.html)

**Companies:** Google, Microsoft

## Description

You are given an integer array,

nums

, and an integer

k

.

nums

comprises of only

0

's and

1

's. In one move,
            you can choose two

adjacent

indices and swap their values.

Return

the

minimum

number of moves required so that

nums

has

k

consecutive

1

's

.

Example 1:

Input:

nums = [1,0,0,1,0,1], k = 2

Output:

1

Explanation:

In 1 move, nums could be [1,0,0,0,

1

,

1

] and have 2 consecutive 1's.

Example 2:

Input:

nums = [1,0,0,0,0,0,1,1], k = 3

Output:

5

Explanation:

In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,

1

,

1

,

1

].

Example 3:

Input:

nums = [1,1,0,1], k = 2

Output:

0

Explanation:

nums already has 2 consecutive 1's.

Constraints:

1 <= nums.length <= 10

5

nums[i]

is

0

or

1

.

1 <= k <= sum(nums)

Difficulty:

Hard

Lock:

Normal

Company:

Google

Microsoft

Problem Solution

1703-Minimum-Adjacent-Swaps-for-K-Consecutive-Ones

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

