# 1025. Divisor Game

**Source:** [https://leetcode.ca/all/1025.html](https://leetcode.ca/all/1025.html)

**Companies:** Visa

## Description

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number

N

on the chalkboard.  On each player's
        turn, that player makes a

move

consisting of:

Choosing any

x

with

0 < x < N

and

N % x ==
            0

.

Replacing the number

N

on the chalkboard with

N -
            x

.

Also, if a player cannot make a move, they lose the game.

Return

True

if and only if Alice wins the game, assuming both players play
        optimally.

Example 1:

Input:

2

Output:

true

Explanation:

Alice chooses 1, and Bob has no more moves.

Example 2:

Input:

3

Output:

false

Explanation:

Alice chooses 1, Bob chooses 1, and Alice has no more moves.

Note:

1 <= N <= 1000

Difficulty:

Easy

Lock:

Normal

Company:

Visa

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

