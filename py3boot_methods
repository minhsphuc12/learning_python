mylist = [1,2,3]
mylist.append(4)
mylist.insert(10,10)
help(my_list2.insert)

'od' in 'doggy'

def myfunc(a,b):
    #return 5% of sum of a and b
    return sum((a,b)) *0.05
    
def myfunc(a, *mo, **co):
    print (mo)
    print (co)
    return sum(mo) * 0.05 * sum(co.values()) / a

a = {'co' : 12, 'do' : 16}
a.values()

myfunc(0.5,2,3,5, b = 100, c = 100)
sum((2,3,5)) * 0.05 * sum((100,100)) / 3


def myfunc (**kwargs):
    if 'fruit' in kwargs:
        print('my fruit is {}'.format(kwargs['fruit']))
    else:
        print('no fruit')
myfunc(fruita = 'apple')

def myfunc(*co, **do):
 #   print (co)
#    print(do)
    print('I like {} {}'.format(co, do))
myfunc(10,20, bo = 100, odo = 44)

co = [1,2,3,4]
list('abc')

3 in range(0,10)
'BC'.isupper()
s = 'aBcDD'
import collections

cnt = collections.Counter()
for up_char in s:
    if up_char.isupper(): cnt['up'] += 1
for low_char in s:
    if low_char.islower(): cnt['low'] += 1
print('No. of Upper case characters : {}'.format(cnt['up']))
print('No. of Lower case characters : {}'.format(cnt['low']))
    
lista = 'hellehádasaa'
list(lista).sort(reverse = True)
sorted(lista)
s = 'abc'
rever = sorted(s, reverse = True)



cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
cnt

import string
alphabet = string.ascii_lowercase
sample_string = 'give me your name'
check = [(x in sample_string.lower()) for x in alphabet]
True*False
bool(1)
a= 'a'
a.upper()
abs(1-2)
L = [1,2,3,6,7]
from itertools import izip, tee

[y - x for x,y in zip(L,L[1:])]

nums = [1,2,3,3,4,3,3.5]
b = list(zip(nums, nums[1:]))
b

[x[0] == x[1] == 3 for x in b]

def multi(list_num):
    output = 1
    for i in list_num:
        output*= i
    return(output)
multi([10,4])

all([True, True, False])

[1,2,3] == [1,2,3]


a = [1, 3, 6, 7, 9, 9,5]
#Return the sum of the numbers in the array, 
#except ignore sections of numbers starting with a 6 
# and extending to the next 9 (every 6 will be followed by at least one 9).

begin = a.index(6)
end = a[begin:].index(9)+1
a = a[:begin]+a[end+begin:]



for i in a:
    for j in a[a.index(i):]:
        #print(j)
        
while index <= len(a):
    
    index += 1
    
[0,0,7] in [1,0,0,7,5]
        
'007' in '10007'
nums = [1,2,4,0,0,0,7,7,5]
spy_list = ''.join([str(x) for x in nums if x in [0,7]])
import math
math.sqrt(100)
return('007' in spy_list)

import math
def is_prime(n):
    #n = 100
    output = True
    for i in range(2, int(math.sqrt(n))+1):
        print(i)
        if n%i == 0:
            output = False
            break
    return(output)  
is_prime(23)
stuff = [1,2,3]
a = map(sum, stuff)
list(map(sum, stuff))

def square(num):
    return num**2

my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))

def splicer(name):
    if len(name) %2 ==0:
        return 'EVEN'
    else:
        return name[0]
        
list(map(splicer, ['Colin','Anna','Ryan']))

def check_even(num):
    if num%2 == 0:
        return True
    else:
        return False
        
list(filter(check_even, [1,2,3,4,4,5,6]))
# get only true condition satisfied

def square(num): return num **2

square = lambda num:num ** 2
lambda num:num ** 2
list(map(lambda num:num**2, nums))
#same with list comprehension
[x**2 for x in nums]

list(filter(lambda num:num%2 == 0, nums))
#same with list comprehension
[x for x in nums if x%2 == 0]

#LEGB rule of scoping
#local
lambda num:num**2 
#enclosing function local
name = 'this is global tring'
def greet():
    name = 'samme'
    def hello():
        print('hello ' + name)
    hello()
    
greet()
#global
name = 'this is global tring'
def greet():
    #name = 'samme'
    def hello():
        print('hello ' + name)
    hello()
    
greet()

x = 100
def myfunc(x):
    #global x 
    #print(f'global x is {x})
    print (f'X is {x}')
    return x
#del(x)

x = myfunc(200)

myfunc()
#built-in
help(len)

