#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
#export PATH=$PATH":$HOME/bin"
import os
from clint.textui import colored
# from tokens import Parser
from shutil import copyfile
import sys

sys.setrecursionlimit(1500)

# try:
#     command = sys.argv[1]
# except:
#     print('"tanzine filename" to run the tanzine code')
#     print('"tanzine startapp app_name" to create an app directory')

#     exit()

# if command.endswith('.tzn'):

#     with open(command) as file:
#         shenzo_parser = Parser(' ')
#         for line in file:
#             shenzo_parser.line += 1
#             shenzo_parser.text = line
#             shenzo_parser.Parse()

# elif command == 'startapp':
#     try:
#         app_name = '/' + sys.argv[2]

#     except:
#         app_name = '/TanzineApp'

#     current_directory = os.getcwd()
#     new_path = os.path.join(current_directory + app_name)

#     try:
#         os.mkdir(new_path)

#     except FileExistsError:
#         print(Fore.RED + f'File {new_path} already exists.' + Fore.RESET)
#         exit()
#     with open(new_path + '/' + 'main.tzn', 'w+') as file:
#         pass

#     os.mkdir(new_path + '/libs')

#     print('Created app at ' + str(new_path))


class TanzineArgumentParser(object):
    def __init__(self, arguments):
        self.arguments = arguments

        print(self.arguments)
