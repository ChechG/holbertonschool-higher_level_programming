#!/usr/bin/python3
"""
4. Text indentation
Write a function that prints a text with 2 new lines 
after each of these characters: ., ? and :
Prototype: def text_indentation(text):"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    j = len(text)
    if text[0] == " ":
            while text[i] == " ":
                i += 1
    while i < j and text[i] != None:
        if text[i] == "\n" and text[i + 1] == " ":
            print("")
            while text[i + 1] == " ":
                i += 1
            i += 1
        if text[i] == None:
                print("")
                break
        while (text[i] == "." or text[i] == "?" or text[i] == ":"):
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                if i == len(text) - 1:
                    break
                print("{}\n".format(text[i]))
                i += 1
                if text[i] == " ":
                    while text[i + 1] == " ":
                        i += 1
                    i += 1
                    continue
        print("{}".format(text[i]), end="")
        i += 1
