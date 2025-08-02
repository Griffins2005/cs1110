"""
Explore conversation tree data

Author:  Lillian Lee (LJL2)
Version: Mar 27, 2025
"""
import os
import json
import utilities

JSON_FILE_NAME = os.path.join('samples','2rpvc7_bench_clearing.json')

print("What is in 2rpvc7_bench_clearing.json?")
with open(JSON_FILE_NAME, 'r') as jfile:
    comment_tree = json.load(jfile)  # list

print(type(comment_tree))

print("How many items are in this list?")
print(len(comment_tree))

print("What does the 'first bit' of the first item look like?")
print(utilities.json_to_pretty(comment_tree[0])[:400])
print()

print("What does the 'first bit' of the second item look like?")
print(utilities.json_to_pretty(comment_tree[1])[:400])
print()

print("What do the keys of the first item look like?")
print(comment_tree[0].keys())
print()

print("How many children does the first item have?")
print(len(comment_tree[0]['data']['children']))
print()

print("What is the text of the submission (the first item in the list)?")
print(comment_tree[0]['data']['children'][0]["data"]["selftext"])
