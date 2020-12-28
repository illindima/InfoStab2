import argparse

def get_init_params():
    parser = argparse.ArgumentParser(description="Лабораторна робота 2, Іллін Дмитро, ІП-04мп")
    
    parser.add_argument("--path", type=str, help="Схема складної системи")
    parser.add_argument("--time", type=int, help="Час безвідмовної роботи елементів системи")
    parser.add_argument("--probability", type=float, nargs="+", help="Ймовірність безвідмовної роботи елементів системи")

    args = parser.parse_args()

    return (args.path, args.time, args.probability)


def prepare_routes(node, routes):
    if len(node.get_children()) == 0:
        temp  = []
        sym_link = node

        while sym_link.get_temp_parent() != None:
            temp.append(sym_link)
            sym_link = sym_link.get_temp_parent()
        
        temp.append(sym_link)
        routes.append(temp)
        return

    for child in node.get_children():
        child.add_temp_parent(node)
        prepare_routes(child, routes)

def prepare_states(size):
    output = []

    def add_binary(num):
        s = []

        while num > 0:
            temp = int(num % 2)
            num = int(num / 2)
            s.append(temp)
        
        return s
    
    for i in range(2 ** size):
        res = add_binary(i)

        if len(res) < size:
            for j in range(len(res)):
                res.append(0)
        output.append(res)

    return output

