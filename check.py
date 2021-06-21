#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This module contain the function for testing, include .expect .within and .runtime "

__author__ = "Austin Wei"

import time, functools, os, sys

# From https://stackoverflow.com/questions/8391411/how-to-block-calls-to-print
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

# Purpose: show the runtime of the tested function
# effect: Produce Outputs
# time: O(1)
def _run_time_d(func):
    @functools.wraps(func)
    def wrapper(f, *args, **kw):
        print("Function: %s" % f.__name__)
        start_time =time.time()
        #study this
        with HiddenPrints():
            a = func(f, *args, **kw)
        runtime = time.time() - start_time
        print("Runtime: %f second" % runtime)
        return func(f, *args, **kw)
    return wrapper

# Purpose: expect(f, i, o) Output a message if the function output
#          does not match the expected output and return false
# Contract: func, any, any -> bool
# Time: O(1)
@_run_time_d
def expect(f, i, o):
    if f(i) != o :
        print("Test failed!")
        sb = "Argument: {argument}"
        sc = "Produce output: {output}"
        sd = "Expected output: {expect}"
        print(sb.format(argument = i))
        print(sc.format(output = f(i)))
        print(sd.format(expect = o))
    else:
        print("Test pass!")



# Purpose: within(f, i, o, ran) Output a message if the function output
#          is not within the error range the expected output and return false
# Contract: func, any, any, float -> bool
# effect: Produce Outputs
# Time: O(1)
@_run_time_d
def within(f, i, o, ran):
    if (abs(f(i) - o) > ran):
        print("Test failed!")
        sb = "Argument: {argument}"
        sc = "Produce output: {output}"
        sd = "Expected output: {expect}"
        se = "Range: {ran}"
        print(sb.format(argument = i))
        print(sc.format(output = f(i)))
        print(sd.format(expect = o))
        print(se.format(ran = ran))
    else:
        print("Test pass!")

# Purpose: show the runtime of a function
# effect:Produce Outputs
# time: O(1)
@_run_time_d
def run_time(f, i):
    pass
    
