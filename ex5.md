# 1. 
The code is interpreted first, then send to the queue and wait for the CPU to run. If the computer is doing something else in the background, or other external factors like over heating will make system's performance unstable, the measurement will be inaccurate.

`timeit` method is simpler and suitable for small code snippet measurements.

`repeat` can give more detailed result of each line or compare code snippets in algorithm. 

# 2. 
`timeit` only needs the average because it's not meant for very detailed test. 

`repeat` need to have all 3 in order to check the algorithm running in different cases and indicate a possible outlier caused by the computer. 
