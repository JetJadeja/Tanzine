import os as os
from clint.textui import colored as TextColor
from lol.prompt import Prompt
from tanzine.tokens import Parser
import sys as sys

sys.setrecursionlimit(1500)


class TanzineArgumentParser(object):
    def __init__(self, arguments):
        self.arguments = arguments

        self.parse_arguments()

    def parse_arguments(self):
        if len(self.arguments) < 1:
            self.throw_argument_error("Insufficient arguments")
        else:
            command = self.arguments[0]
            if command == "new":
                try:
                    project_name = Prompt("Project Name").prompt()
                    self.create_project(project_name)
                except Exception as exception:
                    sys.exit()
            else:
                if command.endswith(".tzn"):
                    with open(command, "r") as read_file:
                        parser = Parser()
                        for line in read_file.read():
                            parser.line += 1
                            parser.text = str(line)
                            parser.Parse()
                else:
                    self.throw_argument_error(f"Invalid arguments : {command}")


    def create_project(self, project_name):
        project_dir = os.path.join(os.getcwd(), project_name)
        if not os.path.exists(project_dir):
            os.mkdir(project_dir)
            os.mkdir(os.path.join(project_dir, "libs"))

            with open(os.path.join(project_dir, "main.tzn"), "w") as file:
                file.write("")
            print(TextColor.green(f"Created project at {project_dir}"))
        else:
            self.throw_argument_error(f"A File or Folder with name {project_name} already exists")

    def throw_argument_error(self, statement):
        print(TextColor.red(statement))
        sys.exit()
