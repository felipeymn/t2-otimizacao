import sys
from time import perf_counter


class Node(object):
    # static variables
    count = 0
    best_path = {
        'distance': 0,
        'nodes': []
    }

    def __init__(self, name=0, parent=None, traveled_distance=0, is_root=False):
        self.name = name
        self.parent = parent
        self.is_root = is_root
        self.traveled_path = []
        self.traveled_distance = traveled_distance
        Node.count += 1
        if is_root:
            Node.best_path['nodes'] = []
            Node.best_path['distance'] = 0
            Node.count = 1

    def travel(self):
        self.traveled_path.extend(self.parent.traveled_path)
        self.traveled_path.append(self.parent)

    def available_neighbours(self, paths):
        neighbours = []
        if (self.name == 0) and (self.is_root == False):  # finished path (returned to root)
            path = [node.name for node in self.traveled_path]
            path.append(0)
            if (self.traveled_distance > Node.best_path['distance']):
                Node.best_path['distance'] = self.traveled_distance
                Node.best_path['distance'] = self.traveled_distance
                Node.best_path['nodes'] = path
            return neighbours
        for i, path in enumerate(paths[self.name]):
            if path:
                names = [node.name for node in self.traveled_path if not node.is_root]
                if i not in names:
                    node = Node(name=i, parent=self, traveled_distance=self.traveled_distance + path)
                    neighbours.append(node)
        return neighbours

    def maximum_walk(self, matrix, bound_enabled=False):
        stack = [self]
        while stack:
            for _ in range(len(stack), 0, -1):
                current = stack.pop(0)
                upperbounds_neighbours = []  # list that carries the upperbound values ​​that will be sorted
                for neighbour in current.available_neighbours(matrix):
                    neighbour.travel()  # branch
                    if bound_enabled:
                        ub = upperbound(neighbour, matrix)
                        if ub > Node.best_path['distance']:  # bound
                            upperbounds_neighbours.append([ub, neighbour])
                    else:
                        stack.insert(0, neighbour)
                if bound_enabled:
                    for upperbound_neighbour in sorted(upperbounds_neighbours, key=lambda u_n: u_n[0]):
                        stack.insert(0, upperbound_neighbour[1])


def upperbound(node, matrix):
    sum = 0
    names = [n.name for n in node.traveled_path]
    for i, line in enumerate(matrix):
        if i not in names:  # if the node is not in the current traveled path, add the max distance that it can travel
            sum += max(line)
    sum += node.traveled_distance  # add the current traveled distance
    return sum


def read_input():
    if sys.stdin.isatty():
        raise FileNotFoundError('Input file not found')
    input_data = []
    for line in sys.stdin:
        input_data.append((list(map(int, line.split(" ")))))
    nodes_count = input_data.pop(0)[0]
    if nodes_count != len(input_data) + 1:
        raise IndexError(
            f'The number of declared nodes is different from expected (declared: {len(input_data)} expected: {nodes_count})')
    return input_data, nodes_count


def create_matrix(data, size):
    # set all lines to the same size
    for links in data:
        for _ in range(size - len(links)):
            links.insert(0, 0)
    data.append([0] * size)  # append the last line, which didnt come with the input data

    # copy the values above main diagonal to create a symmetric matrix
    for i in range(size):
        for j in range(i+1, size):
            data[j][i] = data[i][j]

    return data


def print_matrix(matrix):
    for i in matrix:
        print('\t'.join(map(str, i)))


def print_stdout():
    print(Node.best_path['distance'])
    # increase node value + 1 to match specification (root node == 1)
    print(' '.join(map(lambda node: str(node+1), Node.best_path['nodes'])))


def print_stderr(start, end):  # number of nodes and time report
    sys.stderr.write(f'Number of created nodes: {Node.count}\n')
    sys.stderr.write(f'Elapsed Time: {end - start}\n')


def main():
    try:
        links, size = read_input()
    except (FileNotFoundError, IndexError, ValueError) as e:
        sys.stderr.write(f'Error: {e}\n')

    matrix = create_matrix(links, size)

    start = perf_counter()
    node = Node(is_root=True)
    node.maximum_walk(matrix, bound_enabled=True)
    end = perf_counter()

    print_stdout()
    print_stderr(start, end)

    start = perf_counter()
    node = Node(is_root=True)
    node.maximum_walk(matrix)
    end = perf_counter()

    print_stdout()
    print_stderr(start, end)


if __name__ == '__main__':
    main()
