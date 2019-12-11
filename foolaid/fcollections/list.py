from forbiddenfruit import curses

from typing import Callable

from functools import reduce


@curses(list, 'map')
def list_map(self, f: Callable) -> list:
    """
    Call map() as a list method.

    :param f: map function to apply to list

    :return: a new list with map function applied
    """

    return list(map(f, self))


@curses(list, 'filter')
def list_filter(self, f: Callable) -> list:
    """
    Call filter() as a list method.

    :param f: filter function to apply to list

    :return: a new list with filter function applied
    """

    return list(filter(f, self))


@curses(list, 'reduce')
def list_reduce(self, f: Callable) -> list:
    """
    Call reduce() as a list method.

    :param f: reduce function to apply to list

    :return: a new list with reduce function applied
    """

    return list(reduce(f, self))