#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""
    
    def __init__(self, data, next_node=None):
        """ Class Constructor """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data Getter """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ data Setter """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ next_node Getter """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ next_node Setter """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Defines a singly linked list """
    def __init__(self):
        """ Class Constructor """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct s
