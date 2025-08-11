# 546. Remove Boxes

**Source:** [https://leetcode.ca/all/546.html](https://leetcode.ca/all/546.html)

**Companies:** Tencent

## Description

Given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you
        can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove
        them and get

k*k

points.

Find the maximum points you can get.

Example 1:

Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]

Output:

23

Explanation:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)

Note:

The number of boxes

n

would not exceed 100.

Difficulty:

Hard

Lock:

Normal

Company:

Tencent

Problem Solution

546-Remove-Boxes

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

