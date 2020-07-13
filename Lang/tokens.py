#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import re
import errors
import traceback
import ast



class Token:
    def __init__(self, _type, value):
        self.type = _type
        self.value = value

    def __repr__(self):
        return f'<Token {self.type}: {self.value}>'

    

class Parser:
    def __init__(self, line):
        self.text = line
        self.position = -1
        self.current = ''
        self.vars = {}
        self.funcs = {}
        self.in_func = False
        self.func_name = ''
        self.func_args = []

    def advance(self):
        self.position += 1
        self.current = self.text[self.position] if self.position < len(self.text) else None

    def new_line(self):
        if self.current == None:
            self.position = -1
    def create_tokens(self):
        tokens_in_line = []

        self.new_line()
        self.advance()

        while self.current != None:
            if self.text[0] not in ['@', '\n', '{', '}', '\'', '"', '\t', ' ']:
                errors.incorrect_first(self.text)
                exit()
            else:
                tokens_in_line.append(self.find_characters())

        return tokens_in_line



    def find_characters(self):
        find = ''

        if self.current == '+':
            find = Token('sPLUS', self.current)

        elif self.current == '-':
            find = Token('sMINUS', self.current)

        elif self.current == '(':
            find = self.find_function()

        elif self.current == ')':
            find = Token('rPAR', self.current)

        elif self.current == '*':
            find = Token('sMULT', self.current)

        elif self.current == '/':
            find = Token('sDIV', self.current)

        elif self.current == '\'':
            find = self.find_others('\'', 'STRING')

        elif self.current == '@':
            find = self.find_others('@', 'sDEF')

        elif self.current.isdigit():
            find = self.find_num()
        
        elif self.current.isalpha():
            find = Token('VAR', self.find_letters())

        elif self.current == '=':
            find = Token('EQTO', self.current)

        elif self.current == '<':
            find = self.find_others('>', 'fNAME')
            self.func_name = find.value

        elif self.current == '[':
            find = self.find_others(']', 'fARGS')
            args_list = find.value
            current = ''
            brack_count = 0
            final = []


            for char in find.value:

                if char == ',' or char == ']':
                    if current[0] == '@':
                        current = current.split('@')[1]
                        self.vars[current] = None
                        final.append(f'self.vars["{current}"]')

                    else:
                        pass


                    current = ''

                else:
                    if char != '[':
                        current += char

            find.value == final
            try:
                self.func_args = final
            except Exception as e:
                print(e)
                errors.syntax_error(self.text)

        elif self.current == '{':

            find = Token('func', 'fSTART')
            self.in_func = True
            self.funcs[self.func_name] = {'args': [], 'lines': []}



        elif self.current == '}':
            find = Token('func', 'fEND')
            self.in_func = False
            self.func_name = ''

        

        self.advance()
        return find

    def find_num(self):
        percount = 0
        num = str(self.current)
        self.advance()
        while percount < 2 and self.current != None and str(self.current) in '1234567890.':
            if self.current in '1234567890.':
                num += self.current

                if self.current == '.':
                    percount += 1

            self.advance()

            
        if num != '':
            if percount >= 1:
                return Token('FLOAT', float(num))

            elif percount == 0:
                return Token('INT', int(num))

        
    def find_others(self, char, itype):
        string = self.current
        char_count = 1
        self.advance()

        while self.current != None and char_count < 2:
            if self.current != char:
                string += self.current

            elif self.current == char:
                char_count += 1
                string += self.current

            self.advance()

        return Token(itype, string)

    def find_letters(self):
        string = str(self.current)
        self.advance()

        while self.current != None and self.current.isalpha():
            string += self.current
            self.advance()

        return string

    def find_function(self):
        function = {}
        func = []
        par_count = 0
        com_count = 0
        args = []

        current = ''

        self.advance()
        while com_count == 0 and par_count < 1 and self.current != None:
            if self.current == ',':
                com_count += 1

            elif self.current == ')':
                par_count += 1

            else:
                current += self.current

            
            self.advance()

        function['name'] = current
        current = ''


        while par_count == 0 and self.current != None:
            if self.current == ',':
                com_count += 1
                
                if current[0] == '@':
                    current = f'self.vars[\'{current[1:]}\']'
                args.append(current)
                current = ''
                self.advance()

            elif self.current == ')':
                par_count += 1
                if current[0] == '@':
                    current = f'self.vars[\'{current[1:]}\']'
                args.append(current)
                current = ''
                self.advance()
                
                break

            elif self.current != ',':
                current += self.current
                self.advance()
            
            
        function['args'] = args
        return Token('RUN', function)

    def find_path(self):
        path = ''
        while self.current != None and [self.current.isalpha() or self.current == '.']:
            path += self.current
            self.advance()

        return path

        
        
    
    def Parse(self):
        line = self.create_tokens()
        if self.in_func == False:
            if type(line) == list:
                iterated_over = []
                completed = []
                final = []

                for obj in line.copy():
                    if type(obj) != Token:
                        line.remove(obj)


                for char in line:
                    index = line.index(char)
                    value = char.value

                    if value not in iterated_over:
                        if value == '@MATH@': #Its math with no variables
                            following_values = [line[index + 1].value, line[index + 2].value, line[index + 3].value]
                            data = eval(f'{str(following_values[0])} {str(following_values[1])} + {str(following_values[2])}')
                            if re.search('[a-zA-Z]', str(data)):
                                completed.append(f"'{data}'")

                            else:
                                completed.append(data)

                            for val in following_values:
                                iterated_over.append(val)

                        if value == '@VAR@':
                            try:
                                var = self.vars[line[index + 1].value]
                            except:
                                var = None
                            completed.append(f'self.vars[\'{line[index + 1].value}\']')

                        if value == '@STRING@':
                            if line[index + 1].type != 'STRING':
                                errors.incorrect_value(self.text, 'STRING', line[index + 1].type, line[index + 1].value)
                            completed.append(str(f'{line[index + 1].value}'))

                            iterated_over.append(line[index + 1])

                        if value in ['@FLOAT@', '@INT@', '@NUM@']:
                            completed.append(line[index + 1].value)
                            iterated_over.append(line[index + 1].value)

                        if value == '@FUNC@':
                            func_name = line[index + 1].value
                            args = line[index + 2].value


                        if value == '@RUN@':
                            try:
                                line[index + 1]
                            except IndexError:
                                errors.syntax_error(self.text)
                            
                            if line[index + 1].type == 'RUN':
                                func = line[index + 1].value['name']
                                args = line[index + 1].value['args']

                                try:
                                    func[0]
                                except IndexError:
                                    errors.invalid_function_name(self.text)

                                if func[0] == '@':
                                    func = func.split('.')
                                    if len(func) > 1:
                                        func[0] = func[0].split('@')[1]

                                    else:
                                        errors.syntax_error()
                                    func = ['', f'self.vars["{func[0]}"].{func[1]}']
                                    
                                elif func[0] == '<':
                                    self.run_functions(func, args)

                                else:
                                    func = func.split('/')
                                    if func[0] != '':
                                        try:
                                            add = f'from {func[0]} import {func[1]}'
                                        except:
                                            errors.function_error(self.text)
                                        exec(add)

                                iterated_over.append(line[index + 1].value)

                                if type(func) == list:
                                    completed.append('{0}({1})'.format(func[1], ', '.join(args)))
                                    
                                


                        if value == '=':
                            completed.append('=')
                            iterated_over.append('=')

            completed = [str(i) for i in completed]           
            statment  = ' '.join(completed)
            try:
                x = exec(statment)
            except SyntaxError:
                '''traceback.print_exc()'''
                errors.syntax_error(self.text)
            except KeyError:
                errors.unknown_variable(self.text)

        else:
            if '@FUNC@' not in self.text:
                self.funcs[self.func_name]['lines'].append(self.text)
                if self.funcs[self.func_name]['args'] != self.func_args:
                    self.funcs[self.func_name]['args'] = self.func_args

                if self.text[-1] == '}':
                    self.in_func = False
                

    def run_functions(self, name, args):
        try:
            function = self.funcs[name]
        except KeyError:
            errors.undefined_function(self.text, name)

        for arg in args:
            index = args.index(arg)

            exec(function["args"][index] + f' = {arg}')


        for line in function['lines']:
            self.text = line
            self.Parse()


    def read_ext(self, file_name):
        try:
            open(file_name).close()

        except:
            errors.incorrect_import(self.text, file_name)

        with open(file_name) as imported:
            in_function = False
            for line in imported:

                for current in line:
                    if current == '<':
                        find = self.find_others('>', 'fNAME')
                        func_name = find.value

                    elif current == '[':
                        find = self.find_others(']', 'fARGS')
                        args_list = find.value
                        current = ''
                        brack_count = 0
                        final = []


                        for char in find.value:
                            if char == ',' or char == ']':
                                if current[0] == '@':
                                    current = current.split('@')[1]
                                    self.vars[current] = None
                                    final.append(f'self.vars["{current}"]')

                                else:
                                    pass


                                current = ''

                            else:
                                if char != '[':
                                    current += char

                        find.value == final
                        try:
                            self.func_args = final
                        except Exception as e:
                            print(e)
                            errors.syntax_error(self.text)

                    elif current == '{':
                        find = Token('func', 'fSTART')
                        self.in_func = True
                        self.funcs[self.func_name] = {'args': [], 'lines': []}


                    elif current == '}':
                        find = Token('func', 'fEND')
                        self.in_func = False
                        self.func_name = ''  

            