#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from colorama import Fore


def incorrect_first(text):
    print(Fore.RED + '\nERROR: No Definitive Statement')
    print(Fore.BLUE + 'Message: This error may have been caused by using an incorrect first character!')
    print(Fore.YELLOW + str(text))
    print(Fore.GREEN + '^^^')

    print(Fore.RESET)

    exit()

def incorrect_value(text, _type, was, obj):
    print(Fore.RED + f'\nERROR: Incorrect Value: {str(obj)} should have been {_type}, but was {was}')
    print(Fore.BLUE + 'Message: This error may have been caused by an incorrect definitive')
    print(Fore.YELLOW + str(text))
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()


def incorrect_import(text, module):
    print(Fore.RED + f'\nError: Incorrect Value, No MODULE named {module}.')
    print(Fore.BLUE + 'Message: This error may have been caused by an incorrect module in an @ADD@ argument')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))
    
    print(Fore.RESET)
    exit()

def incorrect_args(text, function):
    print(Fore.RED + '\nIncorrect Function Arguments')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def syntax_error(text):
    print(Fore.RED + '\nError: Incorrect Syntax')
    print(Fore.BLUE + 'Message: This may have been caused by an incorrect definitive')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def function_error(text):
    print(Fore.RED + '\nError: Incorrect Function')
    print(Fore.BLUE + 'Message: This may have been caused by no "/"')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def eof_error(text, current):
    print(Fore.RED + '\nError: Unexpected EOF during parsing with text' + current)
    print(Fore.BLUE + f'Message: This error may have been caused by a missing {current[0]} at the end of {current}')    
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))
    print(Fore.RESET)

    exit()

def incorrect_filename(text, filename):
    print(Fore.RED + '\nError: Could not open ' + Fore.BLUE +  filename + Fore.RED + '.')
    print(Fore.BLUE + 'Message: This error may have been caused by an incorrect filename')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)

def undefined_function(text, name):
    print(Fore.RED + f'\nError: Function {name} referenced before definition!')
    print(Fore.BLUE + 'Message: This error may have been caused by a wrong function name')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def invalid_function_name(text):
    print(Fore.RED + '\nError: Invalid Funtion Name')
    print(Fore.BLUE + 'Message: This error may have been caused by a function name starting with ","')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def invalid_line(text):
    print(Fore.RED + '\nError: Invalid Line')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def unknown_variable(text):
    print(Fore.RED + f'\nError: Undefined Variable')
    print(Fore.BLUE + 'This error may have been caused by a misspelled variable name')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def no_return(text, func_name):
    print(Fore.RED + f'\nError: {func_name} lacks a @RETURN@ definitive at the end')
    print(Fore.BLUE + 'Message: Please add a return definitive on the last line')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def no_args(text, func_name):
    print(Fore.RED + f'\nError: {func_name} has no arguments')
    print(Fore.BLUE + 'Message: Please add arguments')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()