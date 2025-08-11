# 1192. Critical Connections in a Network

**Source:** [https://leetcode.ca/all/1192.html](https://leetcode.ca/all/1192.html)

**Companies:** Amazon

## Description

There are

n

servers numbered from

0

to

n-1

connected by undirected server-to-server

connections

forming a network
        where

connections[i] = [a, b]

represents a connection between servers

a

and

b

. Any server can reach any other server directly or
        indirectly through the network.

A

critical connection

is a connection that, if removed, will make some server
        unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input:

n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]

Output:

[[1,3]]

Explanation:

[[3,1]] is also accepted.

Constraints:

1 <= n <= 10^5

n-1 <= connections.length <= 10^5

connections[i][0] != connections[i][1]

There are no repeated connections.

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

Problem Solution

1192-Critical-Connections-in-a-Network

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

