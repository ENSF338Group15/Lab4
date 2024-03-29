1. Arrays have a pre-defined data size and allow for random access through indexing while Linked Lists have a dynamic data size and require traversing through each element for access. Insertion and deletions of elements for Linked lists are 0(1) once the position is known but are 0(n) for Arrays since each element needs to be shifted to accommodate.

2. To implement a replace function that acts as a deletion followed by an insertion, after the deletion of the element, we would directly insert the new element at that index, reducing the need to shift elements in the array.

3. Insertion Sort: Implementing insertion sort into a doubly linked list would be feasible as we can traverse and compare elements with its predecessors. When the correct position is found, we can delete the current node and insert the node into its new position. Insertion sort is done in-place.
Merge Sort: Implementing merge sort into a doubly linked list would not be feasible as it would cause nodes to lose the addresses of their next pointer when dividing the doubly linked list. This is because merge sort requires extra memory space as it is done not in-place.

4. The expected complexity for the insertion sort implementation would be 0(n^3) The complexity of applying insertion sort to a regular array would be 0(n^2). This is because a doubly linked list requires traversing through elements to access an element while arrays have random access through indexing.
The expected complexity for the merge sort implementation would be 0(n^2(log(n))). The complexity of applying merge sort to a regular array would be 0(n(log(n))). This is because a doubly linked list requires traversing through elements to access an element while arrays have random access through indexing.
