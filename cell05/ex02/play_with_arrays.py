#!/usr/bin/env python

arr = [2, 8, 9, 48, 8, 22, -12, 2]

print(arr)

result = []

for n in arr:
    if n > 5:
        result.append(n + 2)

print(result)