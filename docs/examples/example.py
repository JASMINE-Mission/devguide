#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Python Style Example

This file illustrates an example of coding styles in Python.
"""


def add_two_lists(list_a, list_b):
    """ calculate two variables

    Returns a new list containing the sum of the elements
    obtained from the two lists. Note that the two lists
    should have the same length.

    Args:
      list_a: left hand side
      list_b: right hand side

    Returns:
      A new list with a series of added elements.
    """
    assert len(list_a) == len(list_b), \
        'the two list should have the same length'
    return [a + b for a, b in zip(list_a, list_b)]
