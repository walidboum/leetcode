# 920. Number of Music Playlists

**Source:** [https://leetcode.ca/all/920.html](https://leetcode.ca/all/920.html)

**Companies:** Coursera, Google, Twitter

## Description

Your music player contains

N

different songs and she wants to listen to

L

(not necessarily different) songs during your trip.  You create a
        playlist so that:

Every song is played at least once

A song can only be played again only if

K

other songs have been
            played

Return the number of possible playlists.

As the answer can be very large,
        return it modulo

10^9 + 7

.

Example 1:

Input:

N =

3

, L =

3

, K =

1

Output:

6

Explanation

:

There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].

Example 2:

Input:

N =

2

, L =

3

, K =

0

Output:

6

Explanation

:

There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]

Example 3:

Input:

N =

2

, L =

3

, K =

1

Output:

2

Explanation

:

There are 2 possible playlists. [1, 2, 1], [2, 1, 2]

Difficulty:

Hard

Lock:

Normal

Company:

Coursera

Google

Twitter

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

