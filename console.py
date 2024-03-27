#!/usr/bin/python3
"""This module is the module Cmd"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The class module"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """the kill signal (ctrl + D)"""
        print()
        return True

    def do_quit(self, line):
        """to quit the console"""
        return True

    def empty(self, line):
        """empty line handling"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
