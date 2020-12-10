#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = dir(hidden_4)
    for n in range(len(list)):
        if list[n][:2] != "__":
            print(list[n])
