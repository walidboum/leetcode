# 332. Reconstruct Itinerary

**Source:** [https://leetcode.ca/all/332.html](https://leetcode.ca/all/332.html)

**Companies:** Amazon, Apple, Bloomberg, Citadel, Facebook, Goldman Sachs, Google, Microsoft, Qualtrics, Snapchat, Twilio, Uber, Yandex, Yelp

## Description

Given a list of airline tickets represented by pairs of departure and arrival airports

[from,
        to]

, reconstruct the itinerary in order. All of the tickets belong to a man who
        departs from

JFK

. Thus, the itinerary must begin with

JFK

.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the
            smallest lexical order when read as a single string. For example, the itinerary

["JFK",
                "LGA"]

has a smaller lexical order than

["JFK",
                "LGB"]

.

All airports are represented by three capital letters (IATA code).

You may assume all tickets form at least one valid itinerary.

Example 1:

Input:

[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

Output:

["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input:

[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

Output:

["JFK","ATL","JFK","SFO","ATL","SFO"]

Explanation:

Another possible reconstruction is

["JFK","SFO","ATL","JFK","ATL","SFO"]

.
             But it is larger in lexical order.

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Apple

Bloomberg

Citadel

Facebook

Goldman Sachs

Google

Microsoft

Qualtrics

Snapchat

Twilio

Uber

Yandex

Yelp

Problem Solution

332-Reconstruct-Itinerary

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

