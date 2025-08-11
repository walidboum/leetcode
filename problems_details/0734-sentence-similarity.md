# 734. Sentence Similarity

**Source:** [https://leetcode.ca/all/734.html](https://leetcode.ca/all/734.html)

**Companies:** Google

## Description

Given two sentences

words1, words2

(each represented as an array of strings),
        and a list of similar word pairs

pairs

, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar,
        if the similar word pairs are

pairs = [["great", "fine"], ["acting","drama"],
            ["skills","talent"]]

.

Note that the similarity relation is not transitive. For example, if "great" and
        "fine" are similar, and "fine" and "good" are similar, "great"
        and "good" are

not

necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being
        similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences

words1 = ["great"],
        words2 = ["great"], pairs = []

are similar, even though there are no
        specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence
        like

words1 = ["great"]

can never be similar to

words2 = ["doubleplus","good"]

.

Note:

The length of

words1

and

words2

will not exceed

1000

.

The length of

pairs

will not exceed

2000

.

The length of each

pairs[i]

will be

2

.

The length of each

words[i]

and

pairs[i][j]

will be in the
            range

[1, 20]

.

Difficulty:

Easy

Lock:

Prime

Company:

Google

Problem Solution

734-Sentence-Similarity

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

