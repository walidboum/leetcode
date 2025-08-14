Below are well‑known problems that exemplify each major algorithmic category discussed earlier, along with concise C# solutions. These selections provide a broad sampling of the techniques commonly needed for interview preparation.

---

## 1. Hashing / Two‑Pointer – “Two Sum”

The classic way to find two numbers in an array that add to a target is to use a hash map to store visited numbers and their indices. As you iterate, look for the complement and return the pair of indices as soon as it’s found.
Given an array of integers that is already ***sorted in ascending order***, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

* Your returned answers (both index1 and index2) are not zero-based.
* You may assume that each input would have *exactly* one solution and you may not use the *same* element twice.

**Example:**
Input: numbers = \[2,7,11,15], target = 9
Output: \[1,2]

Explanation: The sum of 2 and 7 is 9.
&#x20;Therefore index1 = 1, index2 = 2.

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

```csharp
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var map = new Dictionary<int,int>();
        for (int i = 0; i < nums.Length; i++) {
            int complement = target - nums[i];
            if (map.TryGetValue(complement, out int j)) {
                return new int[] { j, i };
            }
            // store index of current element
            map[nums[i]] = i;
        }
        return Array.Empty<int>(); // no solution expected due to problem constraints
    }
}
```

---

## 2. Linked‑List Manipulation – “Add Two Numbers”

To add two numbers represented by linked lists in reverse order, traverse both lists while managing a carry. Append each sum digit to a new list. The approach runs in `O(max(m,n))` time and `O(1)` extra space.
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

```csharp
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry > 0) {
            int sum = carry;
            if (l1 != null) { sum += l1.val; l1 = l1.next; }
            if (l2 != null) { sum += l2.val; l2 = l2.next; }
            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
        }
        return dummy.next;
    }
}
```

---

## 3. Sliding Window – “Longest Substring Without Repeating Characters”

Maintain a window and a set of characters; expand the window while there are no duplicates, shrink when a duplicate appears. Track the maximum window length.

Given a string, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

```csharp
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var seen = new HashSet<char>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.Length; right++) {
            char c = s[right];
            while (seen.Contains(c)) {
                seen.Remove(s[left]);
                left++;
            }
            seen.Add(c);
            maxLen = Math.Max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

---

## 4. Divide & Conquer / Binary Search – “Median of Two Sorted Arrays”

An `O(log(min(m,n)))` solution repeatedly compares medians and discards half the search space. The code below partitions arrays so that all elements on the left of the partition are less than or equal to those on the right.

There are two sorted arrays **nums1** and **nums2** of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.

**Example 1:**

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example 2:**

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

```csharp
public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        // ensure nums1 is the smaller array
        if (nums1.Length > nums2.Length) 
            return FindMedianSortedArrays(nums2, nums1);

        int m = nums1.Length, n = nums2.Length;
        int left = 0, right = m;
        while (true) {
            int i = (left + right) / 2;          // partition nums1
            int j = (m + n + 1) / 2 - i;         // partition nums2

            int maxLeftA  = (i == 0) ? int.MinValue : nums1[i - 1];
            int minRightA = (i == m) ? int.MaxValue : nums1[i];
            int maxLeftB  = (j == 0) ? int.MinValue : nums2[j - 1];
            int minRightB = (j == n) ? int.MaxValue : nums2[j];

            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                // correct partition
                if ((m + n) % 2 == 0) {
                    return ((double)Math.Max(maxLeftA, maxLeftB) +
                            Math.Min(minRightA, minRightB)) / 2.0;
                } else {
                    return (double)Math.Max(maxLeftA, maxLeftB);
                }
            } else if (maxLeftA > minRightB) {
                // move left in nums1
                right = i - 1;
            } else {
                // move right in nums1
                left = i + 1;
            }
        }
    }
}
```

---

## 5. Dynamic Programming / Expand Around Center – “Longest Palindromic Substring”

For each character and the gap between characters, expand outward to find the longest palindrome. This runs in `O(n²)` time and `O(1)` space.

Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

**Example 1:**

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

```

**Example 2:**

```
Input: "cbbd"
Output: "bb"

```

```csharp
public class Solution {
    public string LongestPalindrome(string s) {
        if (string.IsNullOrEmpty(s)) return "";
        int start = 0, maxLen = 1;

        for (int i = 0; i < s.Length; i++) {
            // odd-length palindromes
            ExpandAroundCenter(s, i, i, ref start, ref maxLen);
            // even-length palindromes
            ExpandAroundCenter(s, i, i + 1, ref start, ref maxLen);
        }
        return s.Substring(start, maxLen);
    }

    private void ExpandAroundCenter(string s, int left, int right, ref int start, ref int maxLen) {
        while (left >= 0 && right < s.Length && s[left] == s[right]) {
            left--;
            right++;
        }
        int len = right - left - 1;
        if (len > maxLen) {
            maxLen = len;
            start = left + 1;
        }
    }
}
```

---

## 6. String Simulation – “ZigZag Conversion”

Simulate writing characters in a zig‑zag pattern over `numRows` rows. Use an array of `StringBuilder` objects, switch direction when reaching the top or bottom row, and finally concatenate all rows.
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R

```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

```csharp
public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows <= 1 || s.Length <= numRows) return s;
        var rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) rows[i] = new StringBuilder();

        int row = 0;
        bool goingDown = true;
        foreach (char c in s) {
            rows[row].Append(c);
            if (row == numRows - 1) goingDown = false;
            else if (row == 0) goingDown = true;
            row += goingDown ? 1 : -1;
        }
        var result = new StringBuilder();
        foreach (var sb in rows) result.Append(sb.ToString());
        return result.ToString();
    }
}
```

---

## 7. Graph & Tree Traversal – “Binary Tree Level Order Traversal”

Breadth‑first search (BFS) is the standard pattern for traversing a binary tree level by level.

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,\\

```
    3
   / \
  9  20
    /  \
   15   7

```

return its level order traversal as:\\

```
[
  [3],
  [9,20],
  [15,7]
]
```

```csharp
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

public class Solution {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        var result = new List<IList<int>>();
        if (root == null) return result;
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Count > 0) {
            int count = queue.Count;
            var level = new List<int>();
            for (int i = 0; i < count; i++) {
                var node = queue.Dequeue();
                level.Add(node.val);
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            result.Add(level);
        }
        return result;
    }
}
```

---

## 8. Backtracking – “Generate Parentheses”

Use recursion to build strings of well‑formed parentheses. Keep track of how many opening and closing parentheses remain, and ensure that you never add a closing parenthesis unless there is a corresponding unmatched opening parenthesis.

Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given *n* = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

```csharp
public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        var result = new List<string>();
        Backtrack(result, "", 0, 0, n);
        return result;
    }

    private void Backtrack(List<string> result, string current, int open, int close, int max) {
        if (current.Length == 2 * max) {
            result.Add(current);
            return;
        }
        if (open < max) {
            Backtrack(result, current + "(", open + 1, close, max);
        }
        if (close < open) {
            Backtrack(result, current + ")", open, close + 1, max);
        }
    }
}
```

---

## 9. Greedy – “Jump Game”

Given an array of non‑negative integers where each element represents the maximum jump length from that position, determine if you can reach the last index. The greedy approach keeps track of the furthest reachable index and updates it while iterating.

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

**Example 1:**

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

**Example 2:**

```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```

```csharp
public class Solution {
    public bool CanJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.Max(maxReach, i + nums[i]);
            if (maxReach >= nums.Length - 1) return true;
        }
        return true;
    }
}
```

---

## 10. Monotonic Stack – “Largest Rectangle in Histogram”

Use a stack to maintain indices of bars in non‑decreasing height order. Pop from the stack when a bar breaks the non‑decreasing property to compute area spans, ensuring an `O(n)` solution.

Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

 


The largest rectangle is shown in the shaded area, which has area = `10` unit.

 

**Example:**

```
Input: [2,1,5,6,2,3]
Output: 10
```

```csharp
public class Solution {
    public int LargestRectangleArea(int[] heights) {
        var stack = new Stack<int>();
        int maxArea = 0;
        int n = heights.Length;

        for (int i = 0; i <= n; i++) {
            int currHeight = (i == n) ? 0 : heights[i];
            while (stack.Count > 0 && currHeight < heights[stack.Peek()]) {
                int h = heights[stack.Pop()];
                int width = stack.Count == 0 ? i : i - stack.Peek() - 1;
                maxArea = Math.Max(maxArea, h * width);
            }
            stack.Push(i);
        }
        return maxArea;
    }
}
```

---

These examples illustrate the core logic for each major category. Mastery of these patterns and their representative problems will prepare you to tackle many other questions in the same category.
