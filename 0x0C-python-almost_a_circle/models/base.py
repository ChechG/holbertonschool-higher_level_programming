#!/usr/bin/python3
"""Write the first class Base"""
import json
import os
import csv


class Base():
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function returns the JSON representation of an obj (str)"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        the_list = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for i in range(len(list_objs)):
                the_list.append(list_objs[i].to_dictionary())
        jstrg = cls.to_json_string(the_list)
        with open(filename, 'w') as MyFile:
            MyFile.write(jstrg)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance"""
        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 2)
        elif (cls.__name__ == "Square"):
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """File to instances"""
        filename = cls.__name__ + ".json"
        the_list = []
        if os.path.isfile(filename):
            with open(filename, 'r') as MyFile:
                File = MyFile.read()
                lista = cls.from_json_string(File)
                for i in lista:
                    the_list.append(cls.create(**i))
            return the_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        new_list = []
        filename = cls.__name__ + '.csv'
        headers = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                new_list.append(list_objs[i].to_dictionary())
            if cls.__name__ == 'Rectangle':
                headers = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                headers = ['id', 'size', 'x', 'y']
            with open(filename, mode='w') as my_file:
                result = csv.DictWriter(my_file, fieldnames=headers)
                result.writerows(new_list)

    @classmethod
    def load_from_file_csv(cls):
        """ load from csv """
        filename = cls.__name__ + ".csv"
        MyList = []
        MyDict = {}
        if os.path.isfile(filename):
            with open(filename) as MyFile:
                csvFile = csv.reader(MyFile, delimiter=',')
                for i in csvFile:
                    TempList = []
                    for j in i:
                        TempList.append(int(j))
                    if cls.__name__ == "Rectangle":
                        keys = ['id', 'width', 'height', 'x', 'y']
                        for x in range(len(TempList)):
                            MyDict[keys[x]] = TempList[x]
                        MyList.append(cls.create(**MyDict))
                    if cls.__name__ == "Square":
                        keys = ['id', 'size', 'x', 'y']
                        for x in range(len(TempList)):
                            MyDict[keys[x]] = TempList[x]
                        MyList.append(cls.create(**MyDict))
        return MyList
