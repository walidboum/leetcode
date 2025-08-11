# 68. Text Justification

**Source:** [https://leetcode.ca/all/68.html](https://leetcode.ca/all/68.html)

**Companies:** Airbnb, Amazon, Apple, Box, Coursera, Facebook, Google, Indeed, Intuit, LinkedIn, Lyft, Microsoft, Pinterest, Robinhood, Snapchat, Twilio, Twitter, Uber

## Description

Given an array of words and a width

maxWidth

, format the text such that each
        line has exactly

maxWidth

characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in
        each line. Pad extra spaces

' '

when necessary so that each line has
        exactly

maxWidth

characters.

Extra spaces between words should be distributed as evenly as possible. If the number of
        spaces on a line do not divide evenly between words, the empty slots on the left will be
        assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no

extra

space is
        inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters
            only.

Each word's length is guaranteed to be greater than 0 and not exceed

maxWidth

.

The input array

words

contains at least one word.

Example 1:

Input:

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

Output:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

Output:

[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Explanation:

Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input:

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

Output:

[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Difficulty:

Hard

Lock:

Normal

Company:

Airbnb

Amazon

Apple

Box

Coursera

Facebook

Google

Indeed

Intuit

LinkedIn

Lyft

Microsoft

Pinterest

Robinhood

Snapchat

Twilio

Twitter

Uber

Problem Solution

68-Text-Justification

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

