#!/usr/bin/python3
import cmd
from models import storage
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
                  "Amenity", "Place", "Review"]
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

    def do_destroy(self, line):
        """Destroy an instance by its ID"""
        args = line.split()
        if not args:
            print(self.class_errors["missing_name"])
        elif args[0] not in this.class_list:
            print(self.class_errors["not_exist"])
        elif len(args) < 2:
            print(self.class_errors["missing_id"])
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                del obj_dict[key]
                storage.save()

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

    def do_update(self, line):
        """Update the attributes of an instance"""
        args = line.split()
        obj_dict = storage.all()
        if not args:
            print(self.class_errors["missing_name"])
        elif args[0] not in self.class_list:
            print(self.class_errors["not_exist"])
        elif len(args) < 2:
            print(self.class_errors["missing_id"])
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                if len(args) < 3:
                    print(self.class_errors["missing_attribute"])
                elif len(args) < 4:
                    print(self.class_errors["missing_value"])
                else:
                    obj = obj_dict[key]
                    setattr(obj, args[2], args[3].replace("\"", ""))
                    obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
