1. Firstly, the outer loop runs `n` times, where `n` is the size of the list. For each element in the list, its time complexity is `O(n)`. Within the loop, the list is traversed for each element to
find the element at the current index which also has a `O(n)` time complexity. Therefore, the overall time complexity is `O(n) * O(n)` which is 
`O(n^2)`.

2. The new code now only iterates through the list once, which changes the next pointer of each node to point to the previous node. Because of this, the new time complexity is now `O(n)`.