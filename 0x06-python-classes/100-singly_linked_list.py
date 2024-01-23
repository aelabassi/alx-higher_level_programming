#!/usr/bin/python3
"""Defines a node of Singly linked list"""


class Node:
    """This class created a node for singly linked list"""
    def __init__(self, data, next_node=None):
        """Init a new Node with data and next node
            Args:
                data (int): node's data
                next_node (Node): next node the current node points to
            """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter: retutns the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter: sets the value of data to value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter: return a node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter: points the node to the next (value)"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Define a singly linked list"""


class SinglyLinkedList:
    """This class defines a singly linked list"""
    def __init__(self):
        """Init a new Singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """traverse a linked list in increasing order"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self) -> str:
        """prints the linked list"""
        data = []
        tmp = self.__head
        while tmp is not None:
            data.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(data)
