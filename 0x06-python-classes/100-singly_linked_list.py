#!/usr/bin/python3
"""Square class"""


class Node:
    def __init__(self, data, next_node=None):
        """Square class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """property setter to set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property to retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property to retrieve next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Square class"""
    def __init__(self):
        """Square class"""
        self.__head = None

    def sorted_insert(self, value):
        """Square class"""
        n = Node(value)
        if self.__head is None:
            n.next_node = None
            self.__head = n
        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n
        else:
            curr = self.__head
            while (curr.next_node is not None and curr.next_node.data < value):
                curr = curr.next_node
            n.next_node = curr.next_node
            curr.next_node = n

    def __str__(self):
        """Square class"""
        datas = []
        curr = self.__head
        while curr is not None:
            datas.append(str(curr.data))
            curr = curr.next_node
        return ('\n'.join(datas))
