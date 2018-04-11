#!/usr/bin/env python
'''
This caching option uses a global dictionary to store results.

This is a better result than using global variables, since we now have "keys"
for each operation.

The downside is (possibly) we need to control key generation, and each function
needs to check the cache.  Not very DRY!
'''
import time
from pprint import pprint as pp

CACHE = {}


def do_long_op_one(arg1, arg2):
    key = 'do_long_op_one|%r|%r' % (arg1, arg2)

    if key in CACHE:
        return CACHE[key]

    # simulate long operation
    time.sleep(5)
    CACHE[key] = arg1 * arg2

    return CACHE[key]


def clear_cache():
    CACHE.clear()


def main():
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    print "The result:", do_long_op_one(3, 4)
    print "The result:", do_long_op_one(3, 4)
    print "The result:", do_long_op_one(10, 10)

    print "CACHE is:"
    pp(CACHE)


if __name__ == '__main__':
    main()
