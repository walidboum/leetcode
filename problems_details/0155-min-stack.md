# 155. Min Stack

**Source:** [https://leetcode.ca/all/155.html](https://leetcode.ca/all/155.html)

**Companies:** Adobe, Amazon, Apple, Bloomberg, Cisco, eBay, Flipkart, GoDaddy, Goldman Sachs, Google, Intuit, LinkedIn, Lyft, Microsoft, Oracle, Pure Storage, Snapchat, Uber, Visa, Walmart Labs, Wish, Zenefits

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant
        time.

push(x) -- Push element x onto stack.

pop() -- Removes the element on top of the stack.

top() -- Get the top element.

getMin() -- Retrieve the minimum element in the stack.

## Examples

### Example

```
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

