#!/usr/bin/env python
'''
This caching option uses a memoizing decorator.

This is much better since our functions don't need to interact with the cache
in any way.

Some downsides:
    Multiple "Cache" objects, one for each function
    Different combinations of same argument values (*args & **kwargs) have
        separate cache entries.  This means that the long function will run
        once for each
    The function is no longer itself (it's been replaced).  This messes with
        logging.
'''
import time
from pprint import pprint as pp


class Cache(object):
    def __init__(self, f):
        self.cache = {}
        self.f = f

    def __call__(self, *args, **kwargs):
        key = "%r|%r|%r" % (self.f, args, kwargs)
        if key not in self.cache:
            print "...inside decorator; creating %s" % key
            self.cache[key] = self.f(*args, **kwargs)

        pp(self.cache)
        return self.cache[key]


@Cache
def do_long_op_one(arg1, arg2):
    time.sleep(5)
    return arg1 * arg2


@Cache
def do_long_op_two(arg1, arg2):
    time.sleep(5)
    return arg1 + arg2


def main():
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    do_long_op_one.cache.clear()
    print "The result:", do_long_op_one(1, 2)
    print "The result:", do_long_op_one(3, 4)
    #######

    print "The result:", do_long_op_two(3, arg2=84)
    print "The result:", do_long_op_two(arg1=3, arg2=84)

    pp(globals())


if __name__ == '__main__':
    main()
