import csv
import math

from node import Node
from utils import get_init_params, prepare_routes, prepare_states


def parse_file(path):
    output = []

    with open(path, newline="\n") as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            output.append(row)

    return output

def main():
    pt = 0
    lt = 0

    resilience = {}
    routes = []

    path_to, time, probability = get_init_params()

    parsed_input = parse_file(path_to)
    tree = []

    for i in range(len(probability)):
        resilience[str(i)] = probability[i]

    for i in range(len(parsed_input)):
        tree.append(Node(str(i)))

    for i in range(len(parsed_input)):
        for j in range(len(parsed_input[i])):
            if parsed_input[i][j] == "1":
                tree[i].add_child(tree[j])

    for node in tree:
        if len(node.get_parents()) == 0:
            prepare_routes(node, routes)

    for index, route in enumerate(routes):
        routes[index] = route[::-1]

    states = prepare_states(len(tree))

    for state in states:
        active = []

        for index in range(len(state)):
            if state[index] == 1:
                active.append(str(index))
        
        for route in routes:
            contains_nodes = True

            for node in route:
                if not (node.get_name() in active):
                    contains_nodes = False
                    break
            
            if contains_nodes:
                current = 1
               
                for key in resilience:
                    val = resilience[key]

                    if key in active:
                        current *= val
                    else:
                        current *= 1 - val

                pt += current
                break
    
    
    lt = -math.log(pt) / time
    tndv = 1 / lt

    print("P(t): ", pt)
    print("λ: ", lt)
    print("Тндв: ", tndv)


if __name__ == "__main__":
    main()