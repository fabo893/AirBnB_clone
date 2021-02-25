#!/usr/bin/python3
"""
    Console Module
"""


import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import ast


cls_dict = {"BaseModel": BaseModel, "User": User, "City": City,
            "State": State, "Amenity": Amenity, "Place": Place,
            "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Class for the console"""

    prompt = '(hbnb) '

    """Commands"""
    def do_EOF(self, args):
        return True

    def do_quit(self, args):
        return True

    def default(self, args):
        try:
            cmd = args.split('.')
            cls = cmd[0]
            arg = cmd[1].strip('()').split('(')
            if arg[0] == 'all':
                self.do_all(cls)
            elif arg[0] == 'count':
                num = FileStorage._FileStorage__objects
                num_list = str(num.keys())
                cls_count = num_list.count(cls)
                print(cls_count)
            elif arg[0] == 'show':
                char = ''
                char = cls + ' ' + arg[1]
                self.do_show(char)
            elif arg[0] == 'destroy':
                char = ''
                char = cls + ' ' + arg[1]
                self.do_destroy(char)
            elif arg[0] == 'update':
                attr = arg[1].split(', ')
                idd = attr[0]
                del attr[0]
                str_dic = ", ".join(attr)
                print(str_dic)
                if attr[0][0] == '{':
                    dic = ast.literal_eval(str_dic)
                    self.dict_update(cls, idd, dic)
                    return
                opt = str(arg[1].replace(',', ''))
                char = cls + ' ' + opt
                self.do_update(char)
            else:
                pass
        except IndexError:
            self.stdout.write('*** Unknown syntax: %s\n' % arg)

    def dict_update(self, clas, idd, dic):
        """Dictionary version of update method"""
        for key, value in dic.items():
            self.do_update(" ".join([clas, idd, key, str(value)]))

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
        elif args not in cls_dict:
            print("** class doesn't exist **")
        else:
            new = cls_dict[args]()
            print(new.id)

    def do_show(self, info):
        if len(info) == 0:
            print("** class name missing **")
            return
        x = info.split(' ')
        if x[0] not in cls_dict.keys():
            print("** class doesn't exist **")
            return
        elif len(x) == 1:
            print("** instance id missing **")
            return
        k = "{:s}.{:s}".format(x[0], x[1])
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if (obj_id == k):
                print(all_objs[obj_id])
                return
        print("** no instance found **")

    def do_destroy(self, info):
        if len(info) == 0:
            print("** class name missing **")
            return
        x = info.split(' ')
        if x[0] not in cls_dict.keys():
            print("** class doesn't exist **")
            return
        elif len(x) == 1:
            print("** instance id missing **")
            return
        k = "{:s}.{:s}".format(x[0], x[1])
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if (obj_id == k):
                all_objs.pop(k)
                storage.__objects = all_objs
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, arg):
        x = []
        if len(arg) == 0:
            all_objs = storage.all()
            for key in all_objs.keys():
                obj = all_objs[key]
                x.append(str(obj))
            print(x)
            return
        else:
            a = arg.split()
            if a[0] in cls_dict:
                all_objs = storage.all()
                for key in all_objs.keys():
                    obj = all_objs[key]
                    k = key.split('.')
                    if k[0] == a[0]:
                        x.append(str(obj))
                print(x)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] in cls_dict.keys():
            if len(args) >= 2:
                k = "{:s}.{:s}".format(args[0], args[1])
                all_objs = storage.all()
                for key in all_objs.keys():
                    if key == k:
                        if len(args) >= 3:
                            if len(args) >= 4:
                                obj = all_objs[k]
                                a = args[2]
                                v = args[3]
                                setattr(obj, a, v)
                                return
                            else:
                                print("** value missing **")
                                return
                        else:
                            print("** attribute name missing **")
                            return
                print("** no instance found **")
                return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return

    """Help documentation"""
    def help_EOF(self):
        print("End-of-file command to exit the program\n")

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_create(self):
        print("Create command to create a new instane of BaseModel\n")

    def help_show(self):
        print("Show command to show the string representation of instance\n")

    def help_destroy(self):
        print("Delete an instance\n")

    def help_all(self):
        print("Prints all string representation of all instances\n")

    def help_update(self):
        print("Updates an instance based on the class\n")

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
