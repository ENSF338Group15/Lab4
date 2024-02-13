class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next_ = None


def find_middle_of_linked_list(start: LinkedList, last: LinkedList=None):
    if start is None:
        return -1
    slow = start
    fast = start.next_
    while True:
        if fast == last:
            return slow
        fast = fast.next_
        if fast == last:
            return slow
        slow = slow.next_
        fast = fast.next_


def binary_search(start, value):
    while True:
        mid = find_middle_of_linked_list(start)
        if mid is None:
            return None


head = LinkedList(1)
head.next_ = LinkedList(2)
head.next_.next_ = LinkedList(4)
head.next_.next_.next_ = LinkedList(6)
head.next_.next_.next_.next_ = LinkedList(7)
head.next_.next_.next_.next_.next_ = LinkedList(10)
head.next_.next_.next_.next_.next_.next_ = LinkedList(15)

print(find_middle_of_linked_list(head).value)
