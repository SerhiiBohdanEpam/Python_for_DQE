import Homework_5_1 as Work

# print('Modiule 2')
# print(Work.a)

# from test_package_py import package_module
# print(package_module.a)
#
# import sys
# print(sys.argv)
# a = sys.argv[1]
# print(a)

# import os
# os.mknod('test_os_module')

# a = open('Homework_5_1.py')
# print(a.read())

def add_info_from_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

a = add_info_from_file('default_content.txt')
print(a)