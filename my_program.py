from main_package import mainscript
from main_package.sub_package import subscript


mainscript.get_main()
subscript.get_sub()


    
def func():
    print('me')

print('ne')

if __name__  == '__main__':
    print('direct run of this file')

else:
    print('imported')
