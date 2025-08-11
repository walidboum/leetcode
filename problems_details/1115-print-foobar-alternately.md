# 1115. Print FooBar Alternately

**Source:** [https://leetcode.ca/all/1115.html](https://leetcode.ca/all/1115.html)

**Companies:** Unknown

## Description

Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}

The same instance of

FooBar

will be passed to two different threads. Thread A
        will call

foo()

while thread B will call

bar()

. Modify
        the given program to output "foobar"

n

times.

Example 1:

Input:

n = 1

Output:

"foobar"

Explanation:

There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.

Example 2:

Input:

n = 2

Output:

"foobarfoobar"

Explanation:

"foobar" is being output 2 times.

Difficulty:

Medium

Lock:

Normal

Company:

Unknown

Problem Solution

1115-Print-FooBar-Alternately

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

