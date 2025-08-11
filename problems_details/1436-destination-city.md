# 1436. Destination City

**Source:** [https://leetcode.ca/all/1436.html](https://leetcode.ca/all/1436.html)

**Companies:** Yelp

## Description

You are given the array

paths

, where

paths[i] =
            [cityA

i

, cityB

i

]

means there exists a direct path
            going from

cityA

i

to

cityB

i

.

Return
                the destination city, that is, the city without any path outgoing to another
                city.

It is guaranteed that the graph of paths forms a line without any loop, therefore,
                there will be exactly one destination city.

Example 1:

Input:

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

Output:

"Sao Paulo"

Explanation:

Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input:

paths = [["B","C"],["D","B"],["C","A"]]

Output:

"A"

Explanation:

All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:

Input:

paths = [["A","Z"]]

Output:

"Z"

Constraints:

1 <= paths.length <= 100

paths[i].length == 2

1 <= cityA

i

.length, cityB

i

.length <=
                    10

cityA

i

!=

cityB

i

All strings consist of lowercase and uppercase English letters and the
                    space character.

Difficulty:

Easy

Lock:

Normal

Company:

Yelp

Problem Solution

1436-Destination-City

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

