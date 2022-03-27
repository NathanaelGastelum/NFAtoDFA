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
from platform import node

# TODO: read input from file 
nfa = {1: {2, 3}, 
        2: "empty",
        3: {4},
        4: "empty"}


def get_powerset(nfa):
    node_set = list(nfa)
    powerset = []

    for i in range(1 << len(node_set)):
        powerset.append([])
        for j in range(len(node_set)):
            if i & (1 << j):
                powerset[i].append(node_set[j])

    return powerset


def nfa_to_dfa(nfa):
    dfa = {}

    for key in nfa.keys():
        dfa[key] = {key}

        if nfa[key] != "empty":
            nodes = deque()
            nodes.append(nfa[key])

            while nodes:
                node = nodes.popleft()

                # Conversion happens here
                if node not in dfa[key] and node != "empty": 
                    dfa[key].update(node)
                    
                    for i in node:
                        nodes.append(nfa[i])

    return dfa


def print_output(nfa):
    print(sorted(get_powerset(nfa), key=len))

    for key, values in nfa_to_dfa(nfa).items():
        print(f"E({key}) = {values}")

print_output(nfa)
