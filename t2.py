import sys


class Node(object):
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)


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


def upperbound(matrix):
    return 0


def create_matrix(data, size):

    # set all lines to the same size
    for links in data:
        for _ in range(size - len(links)):
            links.insert(0, '0')
    data.append([0] * size)  # append the last line, which didnt come with the input data

    # copy the values above main diagonal to create a symmetric matrix
    for i in range(size):
        for j in range(i+1, size):
            data[j][i] = data[i][j]

    return data


def print_matrix(matrix):
    for i in matrix:
        print('\t'.join(map(str, i)))


def main():
    try:
        links, size = read_input()
    except (FileNotFoundError, IndexError, ValueError) as e:
        sys.stderr.write(f'Error: {e}\n')

    matrix = create_matrix(links, size)
    print_matrix(matrix)

    # t = Node('*', [Node('1'), Node('2'), Node('+', [Node('3'), Node('4')])])


if __name__ == '__main__':
    main()
