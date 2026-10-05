#!/usr/bin/env python3


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    d = {'language': 'C', 'number': 89, 'track': 'Low level'}
    print(update_dictionary(d, 'language', 'Python'))
    print(update_dictionary(d, 'city', 'San Francisco'))
