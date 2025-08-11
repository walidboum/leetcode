# 1258. Synonymous Sentences

**Source:** [https://leetcode.ca/all/1258.html](https://leetcode.ca/all/1258.html)

**Companies:** Cruise Automation

## Description

Given a list of pairs of equivalent words

synonyms

and a sentence

text

, Return all possible synonymous sentences

sorted
                lexicographically

.

Example 1:

Input:

synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"

Output:

["I am cheerful today but was sad yesterday",
âââââââ"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]

Constraints:

0 <= synonyms.length <= 10

synonyms[i].length == 2

synonyms[0] != synonyms[1]

All words consist of at most

10

English letters only.

text

is a single space separated sentence of at most

10

words.

Difficulty:

Medium

Lock:

Prime

Company:

Cruise Automation

Problem Solution

1258-Synonymous-Sentences

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

