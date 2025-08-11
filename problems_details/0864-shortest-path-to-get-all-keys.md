# 864. Shortest Path to Get All Keys

**Source:** [https://leetcode.ca/all/864.html](https://leetcode.ca/all/864.html)

**Companies:** Airbnb, Google

## Description

We are given a 2-dimensional

grid

.

"."

is an
        empty cell,

"#"

is a wall,

"@"

is the
        starting point, (

"a"

,

"b"

, ...) are keys, and
        (

"A"

,

"B"

, ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4
        cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we
        walk over a key, we pick it up.  We can't walk over a lock unless we have the
        corresponding key.

For some

1 <= K <= 6

, there is exactly one lowercase and
        one uppercase letter of the first

K

letters of the English alphabet in the
        grid.  This means that there is exactly one key for each lock, and one lock for each
        key; and also that the letters used to represent the keys and locks were chosen in the
        same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible,
        return

-1

.

Example 1:

Input:

["@.a.#","###.#","b.A.B"]

Output:

8

Example 2:

Input:

["@..aA","..B#.","....b"]

Output:

6

Difficulty:

Hard

Lock:

Normal

Company:

Airbnb

Google

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

