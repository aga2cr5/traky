# -*- coding: utf-8 -*-
def my_sort(lst):
    helplist = []
    """Return the sequence `lst` sorted in-place in ascending order."""
    #​‌‌‌​​​​‌‌​‌‌‌​ Note: in-place means, that the method shouldn't create and return
    #​‌‌‌​​​​‌‌​‌‌‌​ another list, but sort the same list object it received, and
    #​‌‌‌​​​​‌‌​‌‌‌​ return it.
    #​‌‌‌​​​​‌‌​‌‌‌​ It is allowed however, to copy values to another list and use it
    #​‌‌‌​​​​‌‌​‌‌‌​ to get the given list sorted. Note that this will take extra
    #​‌‌‌​​​​‌‌​‌‌‌​ memory though.
    #​‌‌‌​​​​‌‌​‌‌‌​ The solution must be fast in order to complete the biggest sorting
    #​‌‌‌​​​​‌‌​‌‌‌​ problems in time before the time runs out and the evaluator
    #​‌‌‌​​​​‌‌​‌‌‌​ terminates the attempt.
    #​‌‌‌​​​​‌‌​‌‌‌​ Note: If you are implementing a recursive mergesort, remember to
    #​‌‌‌​​​​‌‌​‌‌‌​ divide only up until a certain sublist size, eg. 20, and then sort
    #​‌‌‌​​​​‌‌​‌‌‌​ the sublist with another method, eg. selection sort. Dividing and
    #​‌‌‌​​​​‌‌​‌‌‌​ recursing up until sublists of size 1 is not effective!
    if len(lst) <= 1:
        return lst


    pituus = len(lst)
    for a in range(1, pituus):
        current = lst[a]
        x = a
        while x > 0 and lst[x-1] > current:
            lst[x] = lst[x-1]
            x = x-1
        lst[x] = current

    return lst
