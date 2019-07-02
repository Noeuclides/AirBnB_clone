#!/usr/bin/python3
"""
module that contains the command interpreter class
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        method of emptyline
        """
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return(True)

    def do_EOF(self, args):
        """
        end of file
        """
        return(True)

if __name__ == '__main__':
    inter = HBNBCommand()
    inter.cmdloop(intro=None)
