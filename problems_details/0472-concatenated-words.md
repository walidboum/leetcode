# 472. Concatenated Words

**Source:** [https://leetcode.ca/all/472.html](https://leetcode.ca/all/472.html)

**Companies:** Amazon, Microsoft

## Description

Given a list of words (

without duplicates

), please write a program that returns all
    concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter
        words in the given array.

## Examples

### Example

```
Example:
Input:
["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output:
["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation:
"catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed
10,000
The length sum of elements in the given array will not exceed
600,000
.
All the input string will only include lower case letters.
The returned elements order does not matter.
```

