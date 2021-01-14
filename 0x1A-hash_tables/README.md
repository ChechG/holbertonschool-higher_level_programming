# --- Everything is object ---

# Background Context
        Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different\
 types of objects.

        BTW, have you ever modified a variable without knowing it or wanting to? I mean:

        ```sh
        >>> a = 1
        >>> b = a
        >>> a = 2
        >>> b
        1
        >>>
        ```

        OK. But what about this?

        ```sh
        >>> l = [1, 2, 3]
        >>> m = l
        >>> l[0] = 'x'
        >>> m
        ['x', 2, 3]
        >>>
        ```

        This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. Yo\
u should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding\
 anything for a few hours.

        Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then bra\
instorm together. Only then you can test in the interpreter.

        It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variab\
le types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.

 Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

        All your answers should be only one line in a file. No space before or after the answer.

# Learning Objectives
       At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
       > What is a hash function
        What makes a good hash function
        What is a hash table, how do they work and how to use them
        What is a collision and what are the main ways of dealing with collisions in the context of a hash table
        What are the advantages and drawbacks of using hash tables
        What are the most common use cases of hash tables

# Requirements

**General**
   - Allowed editors: vi, vim, emacs
   - All your files will be compiled on Ubuntu 14.04 LTS
   - Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
   - All your files should end with a new line
   - A README.md file, at the root of the folder of the project is mandatory
   - Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
   - You are not allowed to use global variables
   - No more than 5 functions per file
   - You are allowed to use the C standard library
   - The prototypes of all your functions should be included in your header file called hash_tables.h
   - Don’t forget to push your header file
   - All your header files should be include guarded

# Tasks:
   - 0 - Write a function that creates a hash table.
   - 1 - Write a hash function implementing the djb2 algorithm.
   - 2 - Write a function that gives you the index of a key.
   - 3 - Write a function that adds an element to the hash table.
   - 4 - Write a function that retrieves a value associated with a key.
   - 5 - Write a function that prints a hash table.
   - 6 - Write a function that deletes a hash table.
