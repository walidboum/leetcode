# 150. Evaluate Reverse Polish Notation

**Source:** [https://leetcode.ca/all/150.html](https://leetcode.ca/all/150.html)

**Companies:** Amazon, Google, LinkedIn, Microsoft, Opendoor, Pure Storage, Uber, Zillow

## Description

Evaluate the value of an arithmetic expression in

Reverse
        Polish Notation

.

Valid operators are

+

,

-

,

*

,

/

. Each
        operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.

The given RPN expression is always valid. That means the expression would always
            evaluate to a result and there won't be any divide by zero operation.

Example 1:

Input:

["2", "1", "+", "3", "*"]

Output:

9

Explanation:

((2 + 1) * 3) = 9

Example 2:

Input:

["4", "13", "5", "/", "+"]

Output:

6

Explanation:

(4 + (13 / 5)) = 6

Example 3:

Input:

["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

Output:

22

Explanation:

((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Google

LinkedIn

Microsoft

Opendoor

Pure Storage

Uber

Zillow

Problem Solution

150-Evaluate-Reverse-Polish-Notation

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

