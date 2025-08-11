# 1052. Grumpy Bookstore Owner

**Source:** [https://leetcode.ca/all/1052.html](https://leetcode.ca/all/1052.html)

**Companies:** Nutanix

## Description

Today, the bookstore owner has a store open for

customers.length

minutes. 
        Every minute, some number of customers (

customers[i]

) enter the store, and all
        those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the
        i-th minute,

grumpy[i] = 1

, otherwise

grumpy[i] = 0

.  When
        the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise
        they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for

X

minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input:

customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3

Output:

16

Explanation:

The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Note:

1 <= X <= customers.length == grumpy.length <= 20000

0 <= customers[i] <= 1000

0 <= grumpy[i] <= 1

Difficulty:

Medium

Lock:

Normal

Company:

Nutanix

Problem Solution

1052-Grumpy-Bookstore-Owner

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

