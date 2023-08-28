#!/usr/bin/python3
def complex_delete(a_dictionary, del_value):
    """Deletes keys with a specific value in a dictionary."""
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value == del_value:
            del a_dictionary[key]
    return a_dictionary
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
