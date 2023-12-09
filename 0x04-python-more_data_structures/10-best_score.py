#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxkey = list(a_dictionary.keys())[0]
    maxvalue = a_dictionary[maxkey]
    for key, value in a_dictionary.items():
        if maxvalue < value:
            maxkey = key
            maxvalue = value
    return maxkey
