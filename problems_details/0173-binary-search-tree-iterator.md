# 173. Binary Search Tree Iterator

**Source:** [https://leetcode.ca/all/173.html](https://leetcode.ca/all/173.html)

**Companies:** Alibaba, Amazon, Apple, Bloomberg, Cisco, eBay, Facebook, Google, LinkedIn, Microsoft, Oracle, Qualtrics, Splunk, Uber

## Description

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with
        the root node of a BST.

Calling

next()

will return the next smallest number in the BST.

## Examples

### Example

```
Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
Note:
next()
and
hasNext()
should run in average O(1) time and uses
            O(
h
) memory, where
h
is the height of the tree.
You may assume that
next()
call will always be valid, that
            is, there will be at least a next smallest number in the BST when
next()
is
            called.
```

