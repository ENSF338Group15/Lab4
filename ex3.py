'''
In lines 43-95, this C function list_resize is part of the Python C API and is used to resize a Python list 
object. The function takes two parameters, a pointer to the list to be resized and the new size for the list.
The strategy used to grow arrays when full, is to over-allocate the memory. This is done to reduce the number
of reallocations. When analyzing the line of code on line 70 (new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;), 
the function calculates the new allocation size plus one eighth of the new size this is determined by >>3, so newsize/8 
and add the existing size 1. Therefore the growth factor is approxiately 1.125. 

'''