# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ A class to describe a list node object
#​‌‌‌​​​​‌‌​‌‌‌​ The node object has the following attributes: obj, follower and predecessor

class ListNode:
    """
    The LinkedList uses ListNode objects to store added values.
    This class will not be tested by the grader.

    Attributes:
      obj: Any object that needs to be stored.
      follower: A ListNode object that follows this (self) ListNode object
        in the linked list.
      predecessor: A ListNode object that precedes this (self) ListNode object
        in the linked list.
    """
    def __init__(self, obj):
        """Initialize a list node object with the value obj."""
        self.obj = obj
        self.follower = None
        self.predecessor = None

    def add_after(self, node):
        """Adds node 'node' as the follower of this node."""
        tmp = self.follower
        self.follower = node
        node.predecessor = self
        node.follower = tmp
        if tmp:
            tmp.predecessor = node

    def remove_after(self):
        """Removes the follower of this node."""
        if self.follower:
            self.follower = self.follower.follower
            if self.follower:
                self.follower.predecessor = self


class UnderflowError(Exception):
    """An error raised when trying to remove one of guardian nodes."""
    def __init__(self):
        super().__init__("Can't remove from an empty list!")


class LinkedList:
    """
    An implementation of a doubly linked list that uses ListNode objects
    to represent nodes in the list. List indexes start from zero.

    The list contains one head and one tail guardian node with the values None.
    These can be used to check if the head or tail has been reached.
    The guardian nodes should not be included when counting the size of the list.
    """
    def __init__(self):
        """Initialize the linked list."""
        self.ListNode = ListNode
        self.head = self.ListNode(None)
        self.tail = self.ListNode(None)
        #​‌‌‌​​​​‌‌​‌‌‌​ An empty list should only have one head node followed by a tail node
        self.head.add_after(self.tail)

    def _get_at(self, n):
        """Return the node at position 'n'."""
        node = self.head
        increment = 0
        while node is not None:
            if increment == n:
                return node
            else:
                node = node.follower
                increment += 1

    def add_first(self, obj):
        """Add the object 'obj' as the first node."""
        if self.head is None:
            new_node = ListNode(obj)
            self.head.add_after(new_node)
            return
        new_node = ListNode(obj)
        new_node.follower = self.head
        self.head.predecessor = new_node
        self.head = new_node


    def add_last(self, obj):
        """Add the object 'obj' as the last node."""
        node = self.head
        while node.follower is not None:
            node = node.follower
        new_node = ListNode(obj)
        node.add_after(new_node)


    def add_position(self, n, obj):
        """Insert the object 'obj' as the 'n'th node."""
        node = self._get_at(n)
        new_node = ListNode(obj)

        predecessor = node.predecessor
        if predecessor:
            predecessor.add_after(new_node)


    def remove_position(self, n):
        """Remove the node at the 'n'th position."""
        node = self._get_at(n)
        if self.head is None:
            return
        #​‌‌‌​​​​‌‌​‌‌‌​Prevent from removing guardian nodes.
        if node is self.tail or node is self.head:
            raise UnderflowError()
        predecessor = node.predecessor
        if predecessor:
            predecessor.remove_after()


    def get_position(self, n):
        """Return the value of the node at the 'n'th position or None
        if there is no node at that position."""
        node = self._get_at(n)
        if node:
            return node.obj
        return None


    def get_size(self):
        """Return the number of objects in the list."""
        size = 0
        node = self.head
        if node.obj is None:
            return 0
        while node.obj is not None:
            size += 1
            node = node.follower
        return size


    def get_max(self):
        """Return the value of the largest node in the list."""
        largest = 0
        node = self.head

        while node is not None:
            if node.obj is None:
                None
            else:
                node.obj > largest
                largest = node.obj
            node = node.follower
        return largest
