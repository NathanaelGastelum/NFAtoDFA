from collections import deque
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()

def get_input():
    nfa = {}
    with open(args.input_file) as file:
        for line in file:
            line = line.split(",", maxsplit=1)
            if line[1].strip() == "empty":
                nfa[int(line[0])] = "empty"
            else:
                nfa[int(line[0])] = {int(x) for x in line[1] if x.isdigit()}

    return nfa


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
    print("State set of the equivalent DFA = ", str(sorted(get_powerset(nfa), key=len)).replace('[', '{').replace(']', "}"))

    for key, values in nfa_to_dfa(nfa).items():
        print(f"E({key}) = {values}")

print_output(get_input())
