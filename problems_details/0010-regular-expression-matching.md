# 10. Regular Expression Matching

**Source:** [https://leetcode.ca/all/10.html](https://leetcode.ca/all/10.html)

**Companies:** Adobe, Airbnb, Alibaba, Amazon, Apple, Bloomberg, ByteDance, Coursera, Cruise Automation, eBay, Facebook, Google, Houzz, Lyft, Microsoft, Oracle, Palantir Technologies, Pocket Gems, Twitter, Uber, VMware, Zulily

## Description

Given an input string (

s

) and a pattern (

p

), implement regular
        expression matching with support for

'.'

and

'*'

.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the

entire

input string (not partial).

Note:

s

could be empty and contains only lowercase letters

a-z

.

p

could be empty and contains only lowercase letters

a-z

, and
            characters like

.

or

*

.

Example 1:

Input:

s = "aa"
p = "a"

Output:

false

Explanation:

"a" does not match the entire string "aa".

Example 2:

Input:

s = "aa"
p = "a*"

Output:

true

Explanation:

'*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:

s = "ab"
p = ".*"

Output:

true

Explanation:

".*" means "zero or more (*) of any character (.)".

Example 4:

Input:

s = "aab"
p = "c*a*b"

Output:

true

Explanation:

c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input:

s = "mississippi"
p = "mis*is*p*."

Output:

false

Difficulty:

Hard

Lock:

Normal

Company:

Adobe

Airbnb

Alibaba

Amazon

Apple

Bloomberg

ByteDance

Coursera

Cruise Automation

eBay

Facebook

Google

Houzz

Lyft

Microsoft

Oracle

Palantir Technologies

Pocket Gems

Twitter

Uber

VMware

Zulily

Problem Solution

10-Regular-Expression-Matching

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

