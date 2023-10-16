#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
import shlex
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class inheriting from cmd"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review", "destroy"]
    class_errors = {
        "missing_name": "** class name missing **",
        "not_exist": "** class doesn't exist **",
        "missing_id": "** instance id missing **",
        "no_instance": "** no instance found **",
        "missing_attribute": "** attribute name missing **",
        "missing_value": "** value missing **"
    }

    def do_EOF(self, line):
        """End-of-file marker"""
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        pass

    def default(self, line):
        if line.endswith(".count()"):
            class_name = line.split(".")[0]
            if class_name in self.class_list:
                count = self.count_instances(class_name)
                print(count)
            else:
                print(self.class_errors["not_exist"])

        elif line.endswith(".all()"):
            class_name = line.split(".")[0]
            if class_name in self.class_list:
                self.show_instances(class_name)
            else:
                print(self.class_errors["not_exist"])

        elif re.match(r"(\w+)\.destroy\(\"([^\"]+)\"\)", line):
            # Pattern matches <class name>.destroy("<instance_id>") format
            match = re.match(r"(\w+)\.destroy\(\"([^\"]+)\"\)", line)
            class_name, instance_id = match.groups()

            if class_name in self.class_list:
                obj_dict = storage.all()
                key = "{}.{}".format(class_name, instance_id)

                if key in obj_dict:
                    del obj_dict[key]
                    storage.save()
                else:
                    print(self.class_errors["no_instance"])
            else:
                print(self.class_errors["not_exist"])
        elif re.match(r"(\w+)\.update\(\"([^\"]+)\", "
                      r"\"([^\"]+)\", \"([^\"]+)\"\)", line):
            match = re.match(r"(\w+)\.update\(\"([^\"]"
                             r"+)\", \"([^\"]+)\", \"([^\"]+)\"\)", line)
            class_name, instance_id, attribute, value = match.groups()

            if class_name in self.class_list:
                obj_dict = storage.all()
                key = "{}.{}".format(class_name, instance_id)

                if key in obj_dict:
                    obj = obj_dict[key]
                    setattr(obj, attribute, value)
                    obj.save()
                else:
                    print(self.class_errors["no_instance"])
            else:
                print(self.class_errors["not_exist"])
        elif re.match(r"(\w+)\.show\(\"([^\"]+)\"\)", line):
            # Pattern matches <class name>.destroy("<instance_id>") format
            match = re.match(r"(\w+)\.show\(\"([^\"]+)\"\)", line)
            class_name, instance_id = match.groups()
            if class_name in self.class_list:
                obj_dict = storage.all()
                key = "{}.{}".format(class_name, instance_id)

                if key in obj_dict:
                    self.show_instances(class_name)
                else:
                    print(self.class_errors["no_instance"])

        else:
            print("Command not recognized")

    def count_instances(self, class_name):
        obj_dict = storage.all()
        count = 0
        for key in obj_dict.keys():
            if key.split('.')[0] == class_name:
                count += 1
        return count

    def show_instances(self, class_name):
        obj_dict = storage.all()
        for key, value in obj_dict.items():
            if key.split('.')[0] == class_name:
                print(value)

    def do_create(self, line):
        """Create a new instance of a class"""
        args = line.split()
        if not args:
            print(self.class_errors["missing_name"])
        elif args[0] not in self.class_list:
            print(self.class_errors["not_exist"])
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Show the details of an instance"""
        args = line.split()
        if not args:
            print(self.class_errors["missing_name"])
        elif args[0] not in self.class_list:
            print(self.class_errors["not_exist"])
        elif len(args) < 2:
            print(self.class_errors["missing_id"])
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print(self.class_errors["no_instance"])

    def do_user_show(self, line):
        """Show user details by ID."""
        args = shlex.split(line)
        if not args:
            print(self.class_errors["missing_id"])
        elif args[0] not in self.class_list:
            print(self.class_errors["not_exist"])
        elif len(args) < 2:
            print(self.class_errors["missing_id"])
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print(self.class_errors["no_instance"])

    def do_destroy(self, line):
        """
        Destroy an instance based on its ID.
        Usage: <class name>.destroy(<id>)
        Example: User.destroy(9aa2abd1-6ca1-4efe-9c6f-519bee7bc300)
        """
        args = shlex.split(line)
        if len(args) != 2:
            print("Invalid command format. Usage: <class name>.destroy(<id>)")
            return

        class_name = args[0]
        instance_id = args[1]

        # Check if the class exists
        if class_name not in self.class_list:
            print(self.class_errors["not_exist"])
            return

        # Construct the key to look for in the storage dictionary
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print(self.class_errors["no_instance"])

    def do_all(self, line):
        """Display all instances of a class or all classes"""
        obj_dict = storage.all()
        if not line:
            for key, value in obj_dict.items():
                print(value)
        else:
            args = line.split()
            if args[0] not in self.class_list:
                print(self.class_errors["not_exist"])
            else:
                for key, value in obj_dict.items():
                    if value.__class__.__name__ == args[0]:
                        print(value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
