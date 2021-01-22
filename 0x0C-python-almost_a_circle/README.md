# --- Almost a circle ---

# Background context
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.
In this project, you will review everything about Python:

        Import
        Exceptions
        Class
        Private attribute
        Getter/Setter
        Class method
        Static method
        Inheritance
        Unittest
        Read/Write file

You will also learn about:

        args and kwargs
        Serialization/Deserialization
        JSON

# Learning Objectives
       At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
       > What is Unit testing and how to implement it in a large project
        How to serialize and deserialize a Class
        How to write and read a JSON file
        What is *args and how to use it
        What is **kwargs and how to use it
        How to handle named arguments in a function

# Requirements

**General**
    **PYTHON SCRIPTS**
   - Allowed editors: vi, vim, emacs
   - All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
   - All your files should end with a new line
   - The first line of all your files should be exactly #!/usr/bin/python3
   - A README.md file, at the root of the folder of the project, is mandatory
   - Your code should use the PEP 8 style (version 1.7.*)
   - All your files must be executable
   - The length of your files will be tested using wc
   - All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
   - All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
   - All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
   - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
   
   **Python Unit Tests**
   - Allowed editors: vi, vim, emacs
   - All your files should end with a new line
   - All your test files should be inside a folder tests
   - You have to use the unittest module
   - All your test files should be python files (extension: .py)
   - All your test files and folders should start with test_
   - Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
   - All your tests should be executed by using this command: python3 -m unittest discover tests
   - You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
   - We strongly encourage you to work together on test cases so that you don’t miss any edge case

# Tasks:
   - 0 - All your files, classes and methods must be unit tested and be PEP 8 validated.
   - 1 - Write the first class Base. Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package. Create a file named models/base.py
   - 2 - Write the class Rectangle that inherits from Base.
   - 3 - Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).
   - 4 - Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
   - 5 - Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
   - 6 - Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
   - 7 - Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.
   - 8 - Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.
   - 9 - Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.
   - 10 -Write the class Square that inherits from Rectangle.
   - 11 - Update the class Square by adding the public getter and setter size.
   - 12 - Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.
   - 13 - Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.
   - 14 - Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.
   - 15 - Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries.
   - 16 - Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file.
   - 17 - Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string.
   - 18 - Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.
   - 19 - Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances.

# Advanced.
   - 20 - 
   - 21 - 
