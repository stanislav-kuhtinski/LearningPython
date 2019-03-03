__author__ = 'stanislav-kuhtinski'

import re


def match_string(my_pattern, my_str):
    name_patter = re.compile(my_pattern)
    does_it_match = re.match(name_patter, my_str)
    return ('Match found - ' + str(bool(does_it_match)))


if __name__ == '__main__':
    searh_pattern = r'My name is .*.'
    print(match_string(searh_pattern, 'My name is Stanislav'))
    print(match_string(searh_pattern, 'My name iss Stanislav'))
    print(match_string(searh_pattern, 'My name is '))
