list_sample = [10 , 'false', 200.3]
dictionary = {'key1': "value1", 'key2': 10}
type(tuple_sample)
tuple_sample = (10, "abc", "get")
set_sample = {"a", "b"}

int = 1.5
type(int)

text = 'abcdefg'
text[3]
text[-4]
text[2:5:2]
text[-1:-4:-1]

text[2] = 'cd'
#return error >> immutabitly
'abc' + 'def'
'abcc ' * 3

'abcc' - 'c'

a = 'BAC CDE'
list(a)


text_1 = "phuc"
text_1 = 'an'
ex_format.format()

ex_format = 'BAC {1} then also {0}'
ex_format.format(b, c)
ex_format = 'BAC {} then also {}'
ex_format.format(b, c)

ex_format = 'BAC {e} then also {d}'
ex_format.format(d = 'phuc',e = 'an')

float_format = '{value:width.precision f}'
result = 6000.00568
print("The result was {r:10.2f}".format(r = result))

name = 'phuc'
print(f'Hello, his name is {name}')
#this is easier to allocate variable to string
print('Hello, his name is {}'.format(name))

list_exp = [1,3,2,4,5,6,7]
pop_stuff = list_exp.pop()
list_exp
list_exp.sort(reverse=TRUE)
a = list_exp.sort()
# a get NoneType >> no return of this method
list_exp.reverse()

dictionary = {'key2': "value1", 'key1': 10}

keys = []
for key in dictionary.keys():
    keys.append(key)

keys.sort()

new_dict = {}
for key in keys:
    new_dict[key] = dictionary[key]

new_dict

d={'k1':[1,2,3]}
d.
d['k1'][1]

dictionary.keys()

for key, value in dictionary.items():
    if value == 'value1':
        print (key)

#mydict = {'george':16,'amber':19, 'nathan': 16}
dictionary.keys()
dictionary.values()
dictionary.items()
''.join(['a','b'])
'abc'[2]
# tuple


t = (1,2,3)
t[1] = 2
#error >> immutable

t[2]
t = (1,1,1,2)
t.count(1)
t.index(2)

#set
some_set = set()
some_set = {34,5,67}
some_set.add(2)
#set do not keep duplicated elements
set([1,1,1,2,2,3])

set('probb')
True
False
None

getme.txt
%%writefile myfile.txt
Stuff happend
first license
second line

myfile = open('myfile.txt')
os.getcwd()
pwd

myfile.read()
myfile.seek(0)
text_1 = myfile.readlines()
text_2 = open("C:\\git\\learning_python\\getme.txt")
text_2.read()
myfile.close()
with open('myfile.txt') as my_new_file:
    content = my_new_file.read()

with open('myfile.txt', mode='r') as my_new_file:
    content = my_new_file.read()

with open('myfile.txt', mode='a') as my_new_file:
    my_new_file.write('stuff')

with open('myfile.txt', mode='r') as my_new_file:
    print(my_new_file.read())

with open('123456', mode = 'w') as f:
    f.write('created')

with open('123456', mode = 'r') as f:
    print(f.read())

1 < 2 < 3 < 5
'a' == 'a' != 'b'
not 1<2

a= 'abcde'
for i in a:
    if i == 'a':
        continue
        #pass
        #break
    print(i)

list(range(0,11,2))

word = 'abcd'
for item in enumerate(word):
    print(item)
    
dict(enumerate(word))

a= [1,2,3,9]
b = [3,4,5]
c = [4,5,8]
zip(a,b,c)
list(zip(a,b,c))
'a' in 'abc'
'key' in {'key': 345}

from random import shuffle
a = ['a', 'b', 'c']
shuffle(a)
a

from random import randint
randint(0,100000)

first = int(input('give me a number:'))

int(first)

mystring = 'colin'
mylist = [letter for letter in mystring]
my_list2 = [x**2 for x in range(1,20) if x%2 == 0]
cel = [0,10,20,30]

results = [x if x%2 == 0 else x*2 for x in range(0,11)]
# abuse that make code hard to read
ml = []
for x in [2,3,4]:
    for y in [100, 200, 300]:
        ml.append(x*y)
    
mylist = [x*y for x in [2,3,4] for y in [1,10,1000]]        

ml = []
for x in range(0,100):
    if x%3 == x%5 == 0:
        ml.append('fizzbuzz')
    elif x%3 == 0:
        ml.append('fizz')
    elif x%5 == 0:
        ml.append('buzz')
    else: ml.append(x)
    
ml

