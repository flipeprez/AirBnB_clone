#!/usr/bin/python3
"""
Console module
Entry point
Uses python cmd
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
import json
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def basename(self):
        bn_list = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
                ]
        return (bn_list)

    def do_create(self, command):
        """
        Create a class instance
        """
        if (len(command) < 1):
            print('** class name missing **')
            return
        if (command not in self.basename()):
            print("** class doesn't exist **")
            return
        com = command.split()
        new_obj = eval(f"{com[0]}()")
        new_obj.save()
        print(new_obj.id)

    def do_show(self, command):
        """
        Prints the string representation of a class instance nased on id
        Usage: show <class_name> <id>
        """
        if (len(command) == 0):
            print('** class name missing **')
            return

        com = command.split()
        if (com[0] not in self.basename()):
            print("** class doesn't exist **")
            return

        if len(com) == 1:
            print("** instance id missing **")
            return

        try:
            print(storage.all()[f'{com[0]}.{com[1]}'])
        except Exception as err:
            print("** no instance found **")

    def do_destroy(self, command):
        """
        Deletes an instance based on the class name and id
        """
        if (len(command) == 0):
            print('** class name missing **')
            return

        com = command.split()
        if (com[0] not in self.basename()):
            print("** class doesn't exist **")
            return

        if len(com) == 1:
            print("** instance id missing **")
            return

        try:
            storage.all().pop(f'{com[0]}.{com[1]}')
            storage.save()
        except Exception as err:
            print("** no instance found **")

    def do_all(self, command):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        com = command.split()
        if (len(command) == 0 or com[0] in self.basename()):
            strd_k = storage.all().items()
            strd = {str(key): str(value) for key, value in strd_k}
            print(strd)
        else:
            if (com[0] not in self.basename()):
                print("** class doesn't exist **")
                return

    def do_update(self, command):
        """
        Updates an instance based on the class name and id
        """
        if (len(command) == 0):
            print('** class name missing **')
            return

        com = command.split()
        if (com[0] not in self.basename()):
            print("** class doesn't exist **")
            return

        if len(com) == 1:
            print("** instance id missing **")
            return

        if len(com) == 2:
            print("** attribute name missing **")
            return

        if len(com) == 3:
            print("** value missing **")
            return

        try:
            dict_k = (f'{com[0]}.{com[1]}')
            checkquote = command.find('\"')
            if (checkquote != -1):
                sp_quot = command.split('"')[1::2]
                com[3] = sp_quot
                setattr(storage.all()[dict_k], com[2], com[3][0])
            else:
                setattr(storage.all()[dict_k], com[2], com[3])
            storage.save()
        except Exception as err:
            print("** no instance found **")

    def emptyline(self):
        '''
        add empty line
        '''
        return

    def do_quit(self, command):
        """
        Exit the program
        Usage: quit
        """
        return True

    def do_EOF(self, command):
        """
        End of File exits the program
        Usage: EOF
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
