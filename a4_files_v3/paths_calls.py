"""
Calls functions in module paths on sample data.

Reddit conversation-tree JSON is described (as "comment trees") in
https://github.com/Pyprohly/reddit-api-doc-notes/blob/main/docs/api-reference/comment_tree.rst

Author: Lillian Lee (LJL2)
Version:  Stubs: Mar 27, 2025
"""
import os
import json
import utilities
import cornellasserts
import paths


# See the output of utilities.backbone()
JSON_FILE_NAME = os.path.join('samples','2rpvc7_bench_clearing.json')
with open(JSON_FILE_NAME, 'r') as jfile:
    comment_tree = json.load(jfile)  # list
pretty_comment_tree = utilities.json_to_pretty(comment_tree)

# A test for correctness of utilities.backbone()
print("Checking backbone() for bench-clearing discussion")
result = utilities.backbone(pretty_comment_tree, 80)
expected = '"author": "The_Aesir9613",\n"name": "t3_2rpvc7",\n"selftext": "\\n\\n_____\\nIt\'s my opinion that bench clearings in baseball hurts t\n--------------------------------------------------------------------------------\n"author": "Kman17",\n"body": "I\'d be a little bit cautious of removing the self-policing elements out\n"name": "t1_cnibo8i",\n"parent_id": "t3_2rpvc7",\n          "author": "The_Aesir9613",\n          "body": "Good points.  I would argue though that Hockey fights aren\'t \n          "name": "t1_cnikfa7",\n          "parent_id": "t1_cnibo8i",\n"author": "CherrySlurpee",\n"body": "They really actually help the sport.\\n\\nBaseball, to most people, is a \n"name": "t1_cni6vol",\n"parent_id": "t3_2rpvc7",\n          "author": "The_Aesir9613",\n          "body": "They can be exciting, yes, but that only means people enjoyed\n          "name": "t1_cni7f98",\n          "parent_id": "t1_cni6vol",\n                    "author": "SOLUNAR",\n                    "body": "&gt; That doesn\'t mean they enjoyed watching baseba\n                    "name": "t1_cniszwq",\n                    "parent_id": "t1_cni7f98",\n                              "author": "The_Aesir9613",\n                              "body": "It\'s not a legitimate argument to say bas\n                              "name": "t1_cnjaebu",\n                              "parent_id": "t1_cniszwq",\n"author": "MageZero",\n"body": " Major League Baseball has not only survived, but flourished for 145 ye\n"name": "t1_cni5tm6",\n"parent_id": "t3_2rpvc7",'
cornellasserts.assert_equals(expected, result)
print()




#See what a (long) argument looks like
print('.........Running paths.longest_thread for tontine conversation.........')
JSON_FILE_NAME = os.path.join('samples','3mzc6u_tontine.json')
with open(JSON_FILE_NAME, 'r') as jfile:
    comment_tree = json.load(jfile)  # list
comment_node = comment_tree[1]["data"]["children"][1]
thread = paths.longest_thread(comment_node)
print('\n..            ..\n..Next speaker..\n..            ..\n'.join(thread))
print()
print()




# See what a delta-awarding thread looks like
print('.........Running path_to_delta for tontine conversation.........')
JSON_FILE_NAME = os.path.join('samples','3mzc6u_tontine.json')
with open(JSON_FILE_NAME, 'r') as jfile:
    comment_tree = json.load(jfile)  # list
for comment_node in comment_tree[1]["data"]["children"]:
    print(f">>>> trying comment_node {comment_node['data']['name']} <<<<")
    subthread = paths.path_to_delta(comment_node)
    print('\n..            ..\n..Next speaker..\n..            ..\n'.join(subthread))
