# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:56:57 2018
If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
@author: Nasdap
"""

''' method 1
loop from 1 to 999
for each number, check if that is multiple of 3 or 5
if yes, add to list
sum the list
'''
import time

def is_multiple(dividend, divisor):
    return(dividend % divisor == 0)

#test
    5%2 == 1
    is_multiple(10,5)
    a = [1,2,346,6]
    for b in a:
        print (b)
#end test
True * False

# return true for at least multiple in the divisor list
def is_multiple_list(dividend, divisor_list):
    result = True
    for divisor in divisor_list:
        result *= not(is_multiple(dividend, divisor))
    return (not result)
    #because is_multiple() return a True value for multiple number
    #and is_multiple_list is or condition, so it has to use multiple negation
    #to transform to OR.

is_multiple_list(20, [3,5])

def m1_wrapper(limit, divisor_list):
    start = time.clock()
    pass_list_m1 = []
    for i in range(limit):
        if is_multiple_list(i, problem_divisor_list):
            pass_list_m1.append(i)
    #return(sum(pass_list_m1))
    stop = time.clock()
    return(stop - start)

problem_divisor_list = [3,5]
problem_limit = 1000

start = time.clock()
#begin execution  
m1_wrapper(100,problem_divisor_list)

stop = time.clock()
#sum(pass_list)

#end execution

time_run_m1 = stop - start
time_run_m1



''' method 2
get the list of multiple number of 3 until 999
get the list of multiple number of 5 until 999
get unique union of those list
sum the list
'''

def get_multiple_list(limit, divisor):
    quotient = (limit-1) // divisor
    multiple_list_core = list(range(quotient+1))
    multiple_list = [x * divisor for x in multiple_list_core]
    return(multiple_list)
    
get_multiple_list(10,5)    
    
def get_multiple_list_combine(limit, divisor_list):
    result = []
    for divisor in divisor_list:
        #result.extend(x for x in get_multiple_list(limit, divisor) if x not in result)
        result = set(list(result) + get_multiple_list(limit, divisor))
    return(result)
    
def m2_wrapper(limit, divisor_list):
    start = time.clock()
    #return(sum(get_multiple_list_combine(limit, divisor_list)))
    sum(get_multiple_list_combine(limit, divisor_list))
    stop = time.clock()
    return(stop - start)

#test
a = list([3,4,5,6])
b = [3,4,7,8]
a.extend(x for x in b if x not in a)
set(a+b)

start = time.clock()
#begin execution  

pass_list_m2 = get_multiple_list_combine(problem_limit, problem_divisor_list)
#sum(pass_list_m2)

#end execution
stop = time.clock()
time_run_m2 = stop - start
time_run_m2

#sum(pass_list_m1) == sum(pass_list_m2)
time_run_m1 > time_run_m2
time_run_m1  / time_run_m2

#method 2 is faster than method 1 for limit less than 10^8

limit_list = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]


runtime_m1 = [m1_wrapper(problem_limit,problem_divisor_list) for problem_limit in limit_list]
runtime_m2 = [m2_wrapper(problem_limit,problem_divisor_list) for problem_limit in limit_list]

#in general, method 2 run faster than method 1 four times.












