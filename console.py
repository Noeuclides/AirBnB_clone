#!/usr/bin/python3
"""
module that contains the command interpreter class
"""

import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_create(self, args):
        """
        create instance
        """
        arg = args.split()

        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print ("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        print string representation of an instance
        """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif arg[1] is None:
            print("** instance id missing **")
        else:
            search_obj = storage.all()
            for obj_id in search_obj.keys():
                my_id = obj_id.split(".")
                if arg[1] == my_id[1]:
                    print(search_obj[obj_id])

    def do_destroy(self, args):
        """
        delete object
        """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif arg[1] is None:
            print("** instance id missing **")
        else:
            search_obj = storage.all()
            for obj_id in search_obj.keys():
                my_id = obj_id.split(".")
                if arg[1] == my_id[1]:
                    del search_obj[obj_id]
                    break

if __name__ == '__main__':
    inter = HBNBCommand()
    inter.cmdloop(intro=None)
