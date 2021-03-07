# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ Implement the missing functions here below

from linkedlist import LinkedList

class Queue:

    #​‌‌‌​​​​‌‌​‌‌‌​ An implementation of a queue structure which utilizes the LinkedList class.

    #​‌‌‌​​​​‌‌​‌‌‌​ Attributes:
    #​‌‌‌​​​​‌‌​‌‌‌​ queue (LinkedList): A linked list that is used to store the objects added into the queue.


    def __init__(self):
        """ Initialize the queue """
        self.queue = LinkedList()


    def enqueue(self, obj):
        """ Adds the object 'obj' at the end of the queue """
        self.queue.add_last(obj)

    def dequeue(self):
        """ Removes and returns the first object in the queue """
        first = self.queue.get_position(0)
        self.queue.remove_position(0)
        return first

    def first(self):
        """ Returns the first object in the queue """
        first = self.queue.get_position(0)
        return first

    def last(self):
        """ Returns the last object in the queue """
        size = self.queue.get_size() - 1
        last = self.queue.get_position(size)
        return last

    def is_empty(self):
        """ Returns true if the queue is empty, otherwise false """
        size = self.queue.get_size()
        if size == 0:
            return True
        return False
