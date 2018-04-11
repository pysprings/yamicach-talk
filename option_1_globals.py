#!/usr/bin/env python
'''
This caching option uses global variables to store results.
'''
import time

LONG_RESULT1 = None


def do_long_op_one(arg1, arg2):
    global LONG_RESULT1

    if LONG_RESULT1 is not None:
        return LONG_RESULT1

    # simulate long operation
    time.sleep(5)

    # store some result
    LONG_RESULT1 = arg1 * arg2

    return LONG_RESULT1


def clear_cache():
    global LONG_RESULT1
    LONG_RESULT1 = None


def main():
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    print time.asctime()
    print "The result:", do_long_op_one(1, 2)
    print "The result:", do_long_op_one(3, 4)
    print "The result:", do_long_op_one(9, 8)
    print "The result:", do_long_op_one(10, 10)

    print 'Mediocre solution, works ok with just a few functions w/o args'
    print 'What about args?'


if __name__ == '__main__':
    main()
