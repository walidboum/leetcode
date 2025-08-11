# 1419. Minimum Number of Frogs Croaking

**Source:** [https://leetcode.ca/all/1419.html](https://leetcode.ca/all/1419.html)

**Companies:** C3.ai

## Description

Given the string

croakOfFrogs

, which represents a combination of the
            string "croak" from different frogs, that is, multiple frogs can croak at the same time,
            so multiple âcroakâ are mixed.

Return the minimum number of

different

frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters âcâ, ârâ, âoâ, âaâ, âkâ

sequentially

. The
                frogs have to print all five letters to finish a croak. If the given string is
                not a combination of valid "croak" return -1.

Example 1:

Input:

croakOfFrogs = "croakcroak"

Output:

1

Explanation:

One frog yelling "croak

"

twice.

Example 2:

Input:

croakOfFrogs = "crcoakroak"

Output:

2

Explanation:

The minimum number of frogs is two. 
The first frog could yell "

cr

c

oak

roak".
The second frog could yell later "cr

c

oak

roak

".

Example 3:

Input:

croakOfFrogs = "croakcrook"

Output:

-1

Explanation:

The given string is an invalid combination of "croak

"

from different frogs.

Example 4:

Input:

croakOfFrogs = "croakcroa"

Output:

-1

Constraints:

1 <= croakOfFrogs.length <= 10^5

All characters in the string are:

'c'

,

'r'

,

'o'

,

'a'

or

'k'

.

Difficulty:

Medium

Lock:

Normal

Company:

C3.ai

Problem Solution

1419-Minimum-Number-of-Frogs-Croaking

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

