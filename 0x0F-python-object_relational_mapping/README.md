# --- JavaScript - Objects, Scopes and Closures ---

# Background context
    In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

# Learning Objectives
       At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

# Requirements

**General**
   - Allowed editors: vi, vim, emacs
   - All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
   - Your files will be executed with MySQLdb version 1.3.x
   - Your files will be executed with SQLAlchemy version 1.2.x
   - All your files should end with a new line
   - The first line of all your files should be exactly #!/usr/bin/python3
   - A README.md file, at the root of the folder of the project, is mandatory
   - Your code should use the PEP 8 style (version 1.7.*)
   - All your files must be executable
   - The length of your files will be tested using wc
   - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
   - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
   - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
   - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
   - You are not allowed to use execute with sqlalchemy

# Tasks:
   - 0 - Write a script that lists all states from the database hbtn_0e_0_usa.
   - 1 - Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
   - 2 - Write a class Rectangle that defines a rectangle.
   - 3 - Write a class Rectangle that defines a rectangle.
   - 4 - Write a class Rectangle that defines a rectangle.
   - 5 - Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js.
   - 6 - Write a class Square that defines a square and inherits from Square of 5-square.js.
   - 7 - Write a function that returns the number of occurrences in a list.
   - 8 - Write a function that returns the reversed version of a list.
   - 9 - Write a function that prints the number of arguments already printed and the new argument value.
   - 10 - Write a function that converts a number from base 10 to another base passed as argument.
