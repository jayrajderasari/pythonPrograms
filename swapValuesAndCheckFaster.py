# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:10:17 2022

@author: Jayraj Derasari
"""
import timeit
start_time=timeit.default_timer()

start_time=timeit.default_timer()

#A.
a=2
b=5
temp=a
a=b
b=temp
print(a,b)
end_time=timeit.default_timer()
exe_time_A = end_time-start_time
print("Execution time:",exe_time_A)


#B.
a=2
b=5
a=a^b
b=a^b
a=a^b
print(a,b)
end_time=timeit.default_timer()
exe_time_B = end_time-start_time
print("Execution time:",exe_time_B)

if exe_time_A<exe_time_B:
    print("Arithmetic is faster")
else:
    print("XOR is faster")

##A is faster than B##