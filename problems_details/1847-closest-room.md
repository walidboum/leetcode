# 1847. Closest Room

**Source:** [https://leetcode.ca/all/1847.html](https://leetcode.ca/all/1847.html)

**Companies:** Amazon

## Description

There is a hotel with

n

rooms. The rooms are represented by a 2D integer array

rooms

where

rooms[i] = [roomId

i

, size

i

]

denotes that there is a room with room number

roomId

i

and size equal to

size

i

. Each

roomId

i

is guaranteed to be

unique

.

You are also given

k

queries in a 2D array

queries

where

queries[j] = [preferred

j

, minSize

j

]

. The answer to the

j

th

query is the room number

id

of a room such that:

The room has a size of

at least

minSize

j

, and

abs(id - preferred

j

)

is

minimized

, where

abs(x)

is the absolute value of

x

.

If there is a

tie

in the absolute difference, then use the room with the

smallest

such

id

. If there is

no such room

, the answer is

-1

.

Return

an array

answer

of length

k

where

answer[j]

contains the answer to the

j

th

query

.

Example 1:

Input:

rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]

Output:

[3,-1,3]

Explanation:

The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.

Example 2:

Input:

rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]

Output:

[2,1,3]

Explanation:

The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.

Constraints:

n == rooms.length

1 <= n <= 10

5

k == queries.length

1 <= k <= 10

4

1 <= roomId

i

, preferred

j

<= 10

7

1 <= size

i

, minSize

j

<= 10

7

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

Problem Solution

Leetcode Solutions Java Python C++

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

