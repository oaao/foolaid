from forbiddenfruit import curses

from typing import Callable


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