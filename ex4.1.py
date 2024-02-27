def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(i, len(li)):
                li[j] *= 2
    return li


"""
1. 
Worst case: O(n^2)
All elements are greater than 5, so the 2 loops will cause n^2 operations.
Average case: O(n^2)
Same as worst case.
Best case: O(n)
All elements are less than or equal to 5, so program will not reach inner loop.
"""


# make the complexity O(n)
def processdata2(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(i, len(li)):
                li[j] *= 2
        else:
            for j in range(i, len(li)):
                li[j] *= 1
    return li


test = [1, 6, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(processdata(test))
test = [1, 6, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(processdata2(test))
