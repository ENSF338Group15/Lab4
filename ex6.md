1. Arrays have a pre-defined data size and allow for random access through indexing while Linked Lists are have a dynamic data size and requires traversing through each elements for access. Insertion and deletions of elements for Linked lists are 0(1) once the position is known but are 0(n) for Arrays each element needs to be shifted to accomodate.
2. To implement a replace function that acts as a deletion followed by insertion, after the deletion, we would directly insert the new element at the index, reducing the need to shift elements in the array.
3. 
Insertion Sort: Implemenenting insertion sort into a doubly linked list would be feasibile as we are able to traverse and compare elements with its predecessors. When the correct position is found, we can delete the current node and insert the node into its new position. Insertion of sort is done in-place.
Merge Sort: Implementing merge sort into a doubly linked list would be not be feasible as it would cause nodes to lose the addresses of their next pointer when dividing the doubly linked list. This is because merge sort requires extra memory space for as it done not in-place 

4. 
The expected complexity for the insetion sort implementation would be 0(n^3) The complexity of applying it to a regular array would be 0(n^2). 
This because a doubly linked lists requires traversing though to access a element while arrays have random access through indexing.

The expected complexity for the merge sort implementation would be 0(n^2(log(n))). The complexity of applying it to a regular array would be 0(n(log(n))). This because a doubly linked lists requires traversing though to access a element while arrays have random access through indexing.
