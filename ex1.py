"""
Question 4:
The complexity is O(n), binary search is O(log n), there are 2 pointers going, so the complexity becomes O(n)
"""
import timeit
from matplotlib import pyplot as plt


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next_ = None

    def find_middle_of_linked_list(self):
        if self.value is None:
            return -1
        slow = self
        fast = self.next_
        while True:
            if fast is None:
                return slow
            fast = fast.next_
            if fast is None:
                return slow
            slow = slow.next_
            fast = fast.next_

    def binary_search(self, target):
        current = self
        while current is not None:
            if current.value == target:
                return True
            current = current.next_
        return False


class Array:
    def __init__(self, array: tuple):
        self.array = array

    def binary_search(self, start, end, value):
        if start > end:
            return -1
        mid = (start + end) // 2
        if self.array[mid] == value:
            return mid
        elif self.array[mid] > value:
            return self.binary_search(start, mid - 1, value)
        else:
            return self.binary_search(mid + 1, end, value)


def part1():
    head = LinkedList(1)
    head.next_ = LinkedList(2)
    head.next_.next_ = LinkedList(4)
    head.next_.next_.next_ = LinkedList(6)
    head.next_.next_.next_.next_ = LinkedList(7)
    head.next_.next_.next_.next_.next_ = LinkedList(10)
    head.next_.next_.next_.next_.next_.next_ = LinkedList(15)
    print(head.find_middle_of_linked_list().value)



def make_linked_list_for_length(length):
    head = LinkedList(0)
    temp_2 = head
    for i in range(1, length + 1):
        temp_1 = LinkedList(i)
        temp_2.next_ = temp_1
        temp_2 = temp_1
    return head


def make_array_for_length(length):
    return Array(tuple(range(length)))


def part5():
    test_sizes = [1000, 2000, 4000, 8000]
    linked_list_times = []
    array_times = []
    for test_size in test_sizes:
        head = make_linked_list_for_length(test_size)
        time_linked_list = timeit.timeit(lambda: head.binary_search(test_size//9*6), number=1000)
        linked_list_times.append(time_linked_list)
        array = make_array_for_length(test_size)
        time_array = timeit.timeit(lambda: array.binary_search(0, test_size, test_size//9*6), number=1000)
        array_times.append(time_array)
    plt.plot(test_sizes, linked_list_times)
    plt.plot(test_sizes, array_times)
    plt.legend(["Linked List", "Array"])
    plt.xlabel("Size of list")
    plt.ylabel("Time taken")
    plt.savefig("ex1part5.png")
    plt.show()


part5()
