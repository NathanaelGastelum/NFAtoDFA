# Input: 
# 1,{2, 3}
# 2,empty
# 3,{4}
# 4,empty

# Output:
# State set of the equivalent DFA = {empty, {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}, {1, 2,
# 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}}
# E(1) = {1,2,3,4}
# E(2) = {2}
# E(3) = {3,4}
# E(4) = {4}

from collections import deque


input = {1: {2, 3}, 
        2: "empty",
        3: {4},
        4: "empty"}

output = {}

for key, values in input.items():
    node_set = {key}
    if input[key] != "empty":
        nodes = deque()
        nodes.append(input[key])
        while nodes:
            node = nodes.popleft()
            if node not in node_set and node != "empty": 
                node_set.add(input[node])
                nodes.append(node)
    output[key] = node_set
