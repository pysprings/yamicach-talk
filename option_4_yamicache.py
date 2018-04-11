#!/usr/bin/env python
'''
This caching option uses yamicache.
http://yamicache.readthedocs.io/en/latest/

Many of the same benefits of the previous example, plus:
    The function is itself
    *args and **kwargs are handled (same values won't cause extra cache entries)
    Single caching object
'''
import time
from pprint import pprint as pp

from yamicache import Cache

cache = Cache(hashing=False)


@cache.cached()
def do_long_op_one(arg1, arg2):
    time.sleep(5)
    return arg1 * arg2


@cache.cached()
def do_long_op_two(arg1, arg2):
    time.sleep(5)
    return arg1 + arg2


class MyClass(object):
    @cache.cached()
    def my_function(self, value):
        return value


def main():
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    print "The result:", do_long_op_one(1, 2)
    print "The result:", do_long_op_one(3, 4)
    #######

    print "The result:", do_long_op_two(3, arg2=84)
    print "The result:", do_long_op_two(arg1=3, arg2=84)

    m = MyClass()
    m.my_function(4)
    m.my_function(value=4)

    print "#####################################"
    print "globals:"
    pp(globals())

    print "#####################################"
    print "data store:"
    pp(cache._data_store)


if __name__ == '__main__':
    main()
