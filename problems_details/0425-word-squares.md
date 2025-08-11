# 425. Word Squares

**Source:** [https://leetcode.ca/all/425.html](https://leetcode.ca/all/425.html)

**Companies:** Google, Oracle

## Description

Given a set of words

(without duplicates)

, find all

word squares

you
        can build from them.

A sequence of words forms a valid word square if the

k

th

row and column
        read the exact same string, where 0 ≤

k

< max(numRows, numColumns).

For example, the word sequence

["ball","area","lead","lady"]

forms a word square
        because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y

Note:

There are at least 1 and at most 1000 words.

All words will have the exact same length.

Word length is at least 1 and at most 5.

Each word contains only lowercase English alphabet

a-z

.

Example 1:

Input:

["area","lead","wall","lady","ball"]

Output:

[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:

The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Example 2:

Input:

["abat","baba","atan","atal"]

Output:

[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:

The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Difficulty:

Hard

Lock:

Prime

Company:

Google

Oracle

Problem Solution

425-Word-Squares

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

