#!/usr/bin/python3
"""
module that contains the command interpreter class
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = "(hbnb) "
    class_list = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review']

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
        elif arg[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            new = eval(arg[0] + "()")
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        print string representation of an instance
        """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif arg[1] is None:
            print("** instance id missing **")
        else:
            search_obj = storage.all()
            s_id = str(arg[0] + "." + arg[1])
            if s_id in search_obj:
                print(search_obj[s_id])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        delete object
        """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif arg[1] is None:
            print("** instance id missing **")
        else:
            search_obj = storage.all()
            s_id = str(arg[0] + "." + arg[1])
            if s_id not in search_obj:
                print("** no instance found **")
            else:
                setattr(eval(arg[0]), s_id, search_obj[s_id])
                del(search_obj[s_id])

    def do_all(self, args):
        """
        print all string representation
        """
        arg = args.split()
        if len(arg) >= 1 and arg[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            obj_list = []
            search_obj = storage.all()
            for key in search_obj.keys():
                name = key.split(".")
                if len(arg) == 0 or arg[0] == name[0]:
                    k = search_obj[key]
                    obj_list.append(str(k))
            print(obj_list)

    def do_update(self, args):
        """
        updates an instance
        """
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        elif len(arg) == 4:
            objs = storage.all()
            s_id = str(arg[0] + "." + arg[1])
            if s_id not in objs:
                print("** no instance found **")
            else:
                for key, value in objs.items():
                    if key == s_id:
                        setattr(value, arg[2], arg[3].strip('"'))
                        storage.save()
                        storage.reload()
        else:
            pass

    def precmd(self, line):
        if "show" in line:
            temp = line.replace(".show", " ")
            temp = temp.replace("(\"", "")
            temp = temp.replace("\")", "")
            return "show {}".format(temp)
        elif ".all(" in line:
            temp = line.split(".")
            return "all {}".format(temp[0])
        else:
            return line


if __name__ == '__main__':
    inter = HBNBCommand()
    inter.cmdloop(intro=None)
