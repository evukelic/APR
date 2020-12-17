import math
import numpy as np
import random


"""
File Helper.py provides static helper methods used in this exercise.
"""


def get_as_binary(value, upper, lower, length):
    """
    Converts value to binary.
    :param value: value for conversion
    :param upper: upper boundary
    :param lower: lower boundary
    :param length: length of a chromosome
    :return: converted data
    """
    return ((value-lower)/(upper-lower))*(math.pow(2, length)-1)


def get_from_binary(value, upper, lower, length):
    """
    Converts value from binary.
    :param value: binary value for conversion
    :param upper: uppper boundary
    :param lower: lower boundary
    :param length: length of a chromosome
    :return: converted data
    """
    return lower + (value / (math.pow(2, length) - 1)) * (upper-lower)


def get_tournament_members(lower, upper, num):
    """
    Gets randomly chosen tournament members.
    :param lower: lower constraint boundary
    :param upper: upper constraint boundary
    :param num: tournament size
    :return: tournament members
    """
    members = []
    for i in range(num):
        member = random.randint(lower, upper)

        while member in members:
            member = random.randint(lower, upper)

        members.append(member)
    return members


def xor(a, b):
    """
    Bitwise xor operation.
    :param a: Fist element
    :param b: Second element
    :return: The result of the xor operation
    """
    result = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result


def random_unit_generator(n):
    """
    Random unit generator, used for the uniform crossover operation.
    :param n: Size of the unit
    :return: Random unit
    """
    rand_chromosome = np.random.randint(2, size=n)
    rand_chromosome_string = ""
    for byte in rand_chromosome:
        rand_chromosome_string += str(byte)

    return rand_chromosome_string


def convert_binary(data, upper, lower, length, get_binary=True):
    """
    Method from converting to or from binary.
    :param data: data for the conversion
    :param upper: upper constraint boundary
    :param lower: lower constraint boundary
    :param length: length of a chromosome
    :param get_binary: True if data will be converted to binary, False otherwise
    """

    if get_binary:
        return get_as_binary(data, upper, lower, length)
    else:
        return get_from_binary(data, upper, lower, length)


