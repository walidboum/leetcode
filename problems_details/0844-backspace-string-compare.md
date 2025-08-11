# 844. Backspace String Compare

**Source:** [https://leetcode.ca/all/844.html](https://leetcode.ca/all/844.html)

**Companies:** Atlassian, Facebook, Google, Oracle, Uber

## Description

Given two strings

S

and

T

, return if they are
        equal when both are typed into empty text editors.

#

means a backspace
        character.

Example 1:

Input:

S =

"ab#c"

, T =

"ad#c"

Output:

true

Explanation

: Both S and T become "ac".

Example 2:

Input:

S =

"ab##"

, T =

"c#d#"

Output:

true

Explanation

: Both S and T become "".

Example 3:

Input:

S =

"a##c"

, T =

"#a#c"

Output:

true

Explanation

: Both S and T become "c".

Example 4:

Input:

S =

"a#c"

, T =

"b"

Output:

false

Explanation

: S becomes "c" while T becomes "b".

Note

:

1 <= S.length <= 200

1 <= T.length <= 200

S

and

T

only contain lowercase letters and

'#'

characters.

Follow up:

Can you solve it in

O(N)

time and

O(1)

space?

Difficulty:

Easy

Lock:

Normal

Company:

Atlassian

Facebook

Google

Oracle

Uber

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

