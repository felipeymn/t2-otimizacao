import sys


class Node(object):
    def __init__(self, name=0, parent=None, is_root=False):
        self.name = name
        self.parent = parent
        self.is_root = is_root
        self.traveled_path = []

    def __repr__(self):
        return f'{self.name}'

    def travel(self):
        self.traveled_path.extend(self.parent.traveled_path)
        if not self.parent.is_root:
            self.traveled_path.append(self.parent)

    def available_neighbours(self, paths):
        neighbour = []
        if (self.name == 0) and (self.is_root == False):
            return neighbour
        for i, path in enumerate(paths[self.name]):
            if path:
                names = [node.name for node in self.traveled_path]
                if i not in names:
                    neighbour.append(Node(name=i, parent=self))
        return neighbour


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


def print_level_order(root, matrix):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        count = len(q)

        while count > 0:
            temp = q.pop(0)
            print(f'{temp.name}', end=' ')
            for neighbour in temp.available_neighbours(matrix):
                neighbour.travel()
                q.append(neighbour)

            count -= 1
        print(' ')


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


def main():
    try:
        links, size = read_input()
    except (FileNotFoundError, IndexError, ValueError) as e:
        sys.stderr.write(f'Error: {e}\n')

    matrix = create_matrix(links, size)
    print('Matrix:')
    print_matrix(matrix)
    print('\nLevel Order Traversal:')
    print_level_order(Node(is_root=True), matrix)


if __name__ == '__main__':
    main()
