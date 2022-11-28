import random
import time


def binary_search(list, beg, end, element):
    """Binary search a list of root nodes, returns an index even when not found."""
    if end >= beg:
        mid = (beg + end) // 2
        if list[mid].get_data() == element:
            return mid
        elif list[mid].get_data() > element:
            return binary_search(list, beg, mid - 1, element)
        else:
            return binary_search(list, mid + 1, end, element)
    else:
        return beg


def binary_search_find(list, beg, end, element):
    """Binary search a list of root nodes, returns -1 if not found."""
    if end >= beg:
        mid = (beg + end) // 2
        if list[mid].get_data() == element:
            return mid
        elif list[mid].get_data() > element:
            return binary_search_find(list, beg, mid - 1, element)
        else:
            return binary_search_find(list, mid + 1, end, element)
    else:
        return -1


class SortedArray:
    """An array containing root nodes from 0.5 to inf with increment of 1.0."""

    def __init__(self):
        self.list = []

    def insert(self, element):
        # Round to the nearest 0.5
        root_data = round(element)
        if element - root_data >= 0:
            root_data += 0.5
        else:
            root_data -= 0.5

        # Binary search for appropraite place and check if it already exists
        found_index = binary_search(self.list, 0, len(self.list) - 1, root_data)
        try:
            if self.list[found_index].get_data() == root_data:
                self.list[found_index].insert(element)
            else:
                self.list.insert(found_index, Node(root_data))
                self.list[found_index].insert(element)
        except IndexError:
            self.list.insert(found_index, Node(root_data))
            self.list[found_index].insert(element)

    def print(self):
        """Calls print on each element of the array."""
        for i in self.list:
            i.print()
            # print('\n')

    def minimum(self, node):
        """Calls minimum on given root node of the array."""
        index = binary_search_find(self.list, 0, len(self.list) - 1, node)
        if (index != -1):
            return self.list[index].minimum()
        else:
            return None

    def maximum(self, node):
        """Calls maximum on given root node of the array."""
        index = binary_search_find(self.list, 0, len(self.list) - 1, node)
        if (index != -1):
            return self.list[index].maximum()
        else:
            return None

    def search(self, element):
        # Round to the nearest 0.5
        root_data = round(element)
        if element - root_data >= 0:
            root_data += 0.5
        else:
            root_data -= 0.5

        index = binary_search_find(self.list, 0, len(self.list) - 1, root_data)
        return self.list[index].search(element)


class Node:
    """The basic element of a binary tree keeping a value and two references to the other nodes."""

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_data(self):
        return self.data

    def insert(self, data):
        """Insert a new Node into a tree in accordance with binary tree rules."""
        temp_node = self
        while (True):
            if data < temp_node.get_data():
                if temp_node.left:
                    temp_node = temp_node.left
                else:
                    temp_node.left = Node(data)
                    break
            elif data > temp_node.get_data():
                if temp_node.right:
                    temp_node = temp_node.right
                else:
                    temp_node.right = Node(data)
                    break
            else:
                break

    def print(self, depth=0, newline=False):
        """Print a graphical representation of the tree."""
        if newline:
            # If we went right - go to a new line and use tab to position the cursor
            pass
            # print('\n' + '\t' * (depth) + '-' * depth + str(self.data) + '\t', end = '')
        else:
            pass
            # print('-' * depth + str(self.data) + '\t', end = '')

        if self.left:
            self.left.print(depth + 1)

        if self.right:
            # Add a newline when traversing right
            self.right.print(depth + 1, True)

    def minimum(self):
        temp_node = self
        while (temp_node.left):
            temp_node = temp_node.left

        return (temp_node.get_data())

    def maximum(self):
        temp_node = self
        while (temp_node.right):
            temp_node = temp_node.right

        return (temp_node.get_data())

    def search(self, element):
        temp_node = self
        while (temp_node):
            if temp_node.get_data() < element:
                temp_node = temp_node.right
            elif temp_node.get_data() > element:
                temp_node = temp_node.left
            else:
                return True

        return False


if __name__ == "__main__":

    a = SortedArray()
    b = SortedArray()
    c = SortedArray()
    d = SortedArray()

    steps = [100, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 100000]
    for iterations in steps:
        a = SortedArray()
        b = SortedArray()
        c = SortedArray()
        d = SortedArray()
        start_s = time.time()
        for i in range(iterations, 0, -1):
            a.insert(i)

        print("is, " + str(iterations) + ", " + str(time.time() - start_s))

        start_c = time.time()
        for _ in range(iterations):
            i = round(random.random() * 10, 2)
            b.insert(i)

        print("ic, " + str(iterations) + ", " + str(time.time() - start_c))

        start_r = time.time()
        for _ in range(iterations):
            i = round(random.random() * 100, 2)
            c.insert(i)

        print("ir, " + str(iterations) + ", " + str(time.time() - start_r))

        start_max = time.time()
        for _ in range(10000):
            i = random.randint(0, 99) + 0.5
            c.maximum(i)

        print("max, " + str(iterations) + ", " + str(time.time() - start_max))

        start_min = time.time()
        for _ in range(10000):
            i = random.randint(0, 99) + 0.5
            c.minimum(i)

        print("min, " + str(iterations) + ", " + str(time.time() - start_min))
