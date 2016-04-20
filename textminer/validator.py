import re


def binary(values):
    '''String must be binary only'''
    return re.match(r'[01]+', values)


def binary_even(value):
    '''Binary string must be even, so it must end in 0.'''
    return re.match(r'([01]+0$)', value)


def hex(values):
    '''String can be either letters, numbers, or a combination.'''
    return re.match(r'^[a-fA-F0-9-]+$', values)


def word(text):
    '''String can contain letters, case-sensitive does not matter, can include
    numbers also.'''
    return re.match(r'^[\w-]*[^\d]$', text)
#
# def words(text):
#     '''String can include letters, numbers, punctuation, and counts'''
#     return re.match(r')
