#!/usr/bin/python3
def function():
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Hola"

    text = list(texto)
    x = 0
    while x < len(text):
        if text[x] == ".":
            print(text[x])
            if text[x + 1] == " ":
            while text[x + 1] == " ":
            x += 1
    print(text[x], end="")
    x += 1
