def add(a,b):
    print(a+b)
    
no1 = 10
no2 = input('give me a number: ')

add(no1,no2)

try:
    result = 10 + 10
except:
    print('invalid data')
else:
    print('nice adding')
    print(result)


try:
    f = open('getme.txt', 'r')
    f.write('write me')
    1+'2'
except TypeError:
    1+3
    print ("Type Error detected")
except OSError:
    print('OS Error detected')
finally:
    print('Always run')
    
def get_int():
    while True:
        try:
            end = int(input('please give me a number: '))
        except:
            print('not number')
            continue
        else:
            print(end)
            break
        finally:
            print('end stuff')
            

get_int()

