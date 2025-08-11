# 1048. Longest String Chain

**Source:** [https://leetcode.ca/all/1048.html](https://leetcode.ca/all/1048.html)

**Companies:** Akuna Capital, Citadel, Google, SAP, Two Sigma, VMware

## Description

Given a list of words, each word consists of English lowercase letters.

Let's say

word1

is a predecessor of

word2

if and only if
        we can add exactly one letter anywhere in

word1

to make it equal to

word2

.  For example,

"abc"

is a
        predecessor of

"abac"

.

A

word chain

is a sequence of words

[word_1, word_2, ..., word_k]

with

k >= 1

, where

word_1

is a predecessor of

word_2

,

word_2

is a predecessor of

word_3

, and so on.

Return the longest possible length of a word chain with words chosen from the given list of

words

.

Example 1:

Input:

["a","b","ba","bca","bda","bdca"]

Output:

4

Explanation

: one of

the longest word chain is "a","ba","bda","bdca".

Note:

1 <= words.length <= 1000

1 <= words[i].length <= 16

words[i]

only consists of English lowercase letters.

Difficulty:

Medium

Lock:

Normal

Company:

Akuna Capital

Citadel

Google

SAP

Two Sigma

VMware

Problem Solution

1048-Longest-String-Chain

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

