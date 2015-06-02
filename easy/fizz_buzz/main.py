#!/usr/bin/python

"""fizz_buzz.py: Reads 3 numbers for each line in a space delimited file
 (fizz, buzz, limit).
For the range of numbers from 1 to limit, print F, B, or FB depending on if the
 number is evenly divisible by fizz, buzz, or both.
If the number is not divisible by either fizz or buzz, print the number
 instead."""

__author__ = 'Joe Strach'
__license__ = "GPL"
__version__ = "1.0.0"

import sys


def main(input_file):
    """Read a file line by line, print the result of fizz_buzz for each line.

    :param input_file: :basestring: Location of a the space delimited text file
    :return: None
    """
    with open(input_file, 'r') as in_file:
        for line in in_file:
            fizz_div, buzz_div, limit = get_data(line)
            print fizz_buzz(fizz_div, buzz_div, limit)

    return


def fizz_buzz(fizz_divisor, buzz_divisor, limit_inclusive):
    """ From 1 to a limited range, return a string of space delimited
     F, FB, or number

    :param fizz_divisor: :int: Number to determine if the number is a fizz
    :param buzz_divisor: :int: Number to determine if the number is a buzz
    :param limit_inclusive: The max number in a range
    :return: Space delimited string of the results
    """
    output = []

    for i in xrange(1, int(limit_inclusive) + 1):
        fizz_buzz_both = ''

        if i % int(fizz_divisor) == 0:
            fizz_buzz_both = 'F'

        if i % int(buzz_divisor) == 0:
            fizz_buzz_both += 'B'

        if fizz_buzz_both:
            output.append(fizz_buzz_both)
        else:
            output.append(str(i))

    return ' '.join(output)


def get_data(file_line):
    return file_line.split(' ')


if __name__ == '__main__':
    main(sys.argv[1])
