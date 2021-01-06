#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
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
  def __init__(self):
    self.__head = None

  def sorted_insert(self, value):
    curr = self.__head
    if curr is None:
        n = Node(value)
        n.data = value
        self.__head = n
        return

    if curr.data > value:
        n = Node(value)
        n.data = value
        n.next_node = curr
        self.head = n
        return

    while curr.next_node is not None:
        if curr.next_node.data > value:
            break
        curr = curr.next_node
    n = Node(value)
    n.data = value
    n.next_node = curr.next_node
    curr.next_node = n
    return

  def __str__(self):
    datas = []
    curr = self.head
    while curr is not None:
      datas.append(str(curr.data))
      curr = curr.next_node
    return ('\n'.join(datas))
