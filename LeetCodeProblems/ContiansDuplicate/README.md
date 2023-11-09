# Thought Process

## LeetCode: 217. Contains Duplicate

My first thought was to create a new Map and set each number into the map using a for loop. Then, I would check if the map had the number already, if it did, I would return true, if not, I would set the number into the map. However, Map allows for duplicate keys, so I utilized a Set instead. This worked and has 73ms runtime and 52.84 mb memory, both beating over 70% of other submissions.

Decent attempt will try to improve on this, via the solution submissions.
