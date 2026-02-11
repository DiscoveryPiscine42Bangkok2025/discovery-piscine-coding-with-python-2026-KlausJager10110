#!/usr/bin/env python

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for x in arr:
    if x > 5:
        new_arr.append(x + 2)

print(arr)
print(new_arr)