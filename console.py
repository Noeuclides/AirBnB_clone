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
            s_id = str(arg[0] + "." + arg[1])
            if s_id in search_obj:
                print(search_obj[s_id])

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
            s_id = str(arg[0] + "." + arg[1])
            if s_id not in search_obj:
                print("** no instance found **")
            else:
                setattr(BaseModel, s_id, search_obj[s_id])
                del search_obj[s_id]                

    def do_all(self, args):
        """
        print all string representation
        """
        arg = args.split()
        if len(arg) >= 1 and arg[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            list = []
            search_obj = storage.all()
            for key in search_obj:
                list.append(str(search_obj[key]))
            print(list)

    def to_update(self):
        """
        updates an instance
        """
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** class doesn't exist **")
            


if __name__ == '__main__':
    inter = HBNBCommand()
    inter.cmdloop(intro=None)
    
