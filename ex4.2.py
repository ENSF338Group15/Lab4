import timeit
from matplotlib import pyplot as plt


def inefficient_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


def efficient_search(array, target):
    l = len(array) // 2
    L = array[:l]
    R = array[l:]
    if len(array) == 1:
        if array[0] == target:
            return 0
        else:
            return -1
    if array[l] == target:
        return l
    if array[l] > target:
        return efficient_search(L, target)
    if array[l] < target:
        return l + efficient_search(R, target)
    return -1


"""
4. Worst case for linear search: O(n)
Worst case for binary search: O(log n)
"""

test_sizes = [100, 1000, 10000, 100000]
inefficient_times = []
efficient_times = []
for test_size in test_sizes:
    arr = list(range(test_size))
    target = test_size // 10 * 8
    inefficient_times.append(timeit.timeit(lambda: inefficient_search(arr, target), number=100))
    efficient_times.append(timeit.timeit(lambda: efficient_search(arr, target), number=100))

plt.plot(test_sizes, inefficient_times, label="inefficient")
plt.plot(test_sizes, efficient_times, label="efficient")
plt.legend()
plt.xlabel("Test Size")
plt.ylabel("Time")
plt.savefig("ex4.2.png")
plt.show()
