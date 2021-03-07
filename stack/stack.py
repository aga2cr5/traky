# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ Implement the missing functions here below

from linkedlist import LinkedList


class Stack:
    """
    An implementation of a stack structure which utilizes the LinkedList class.

    Attributes:
        stack (LinkedList): A linked list that is used to store the objects added into the stack.
    """
    def __init__(self):
        """Initialize the stack."""
        self.stack = LinkedList()

    def push(self, obj):
        """Add the object 'obj' to the stack."""
        self.stack.add_last(obj)

    def pop(self):
        """Return and remove the newest (previously added) object from the stack."""
        size = self.stack.get_size() - 1
        print(size)
        newest = self.stack.get_position(size)
        print(newest)
        self.stack.remove_position(size)
        return newest

    def top(self):
        """Return the newest (previously added) object."""
        size = self.stack.get_size() - 1
        newest = self.stack.get_position(size)
        return newest

    def is_empty(self):
        """If stack has no objects, return True, else return False."""
        size = self.stack.get_size()
        if size == 0:
            return True
        return False
