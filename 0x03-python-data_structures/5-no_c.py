#!/usr/bin/python3
# Author: Hanif Miyanji
def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
