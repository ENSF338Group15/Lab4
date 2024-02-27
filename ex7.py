import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def get_element_at_pos(self, index):
        node = self.head
        for _ in range(index):
            if node is None:
                return None
            node = node.next
        return node

    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    def optimized_reverse(self):
        prevNode = None
        currNode = self.head
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode

def generate_list(n):
    linked_list = LinkedList()
    for i in range(n):
        node = Node(i)
        node.next = linked_list.head
        linked_list.head = node
    return linked_list

def time_methods(n):
    linked_list = generate_list(n)

    start_time = timeit.default_timer()
    for _ in range(100):
        linked_list_copy = linked_list
        linked_list_copy.reverse()
    end_time = timeit.default_timer()
    reverse_time = end_time - start_time

    start_time = timeit.default_timer()
    for _ in range(100):
        linked_list_copy = linked_list
        linked_list_copy.optimized_reverse()
    end_time = timeit.default_timer()
    optimized_reverse_time = end_time - start_time

    return reverse_time, optimized_reverse_time

sizes = [1000, 2000, 3000, 4000]
reverse_times = []
optimized_reverse_times = []

for size in sizes:
    reverse_time, optimized_reverse_time = time_methods(size)
    reverse_times.append(reverse_time)
    optimized_reverse_times.append(optimized_reverse_time)

plt.plot(sizes, reverse_times, label='reverse')
plt.plot(sizes, optimized_reverse_times, label='optimized_reverse')
plt.xlabel('List size')
plt.ylabel('Execution time (s)')
plt.legend()
plt.show()