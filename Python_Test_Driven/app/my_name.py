#!/usr/bin/python3

def say_my_name(first_name, last_name):

    if not isinstance(first_name, (str)) or not (last_name, (str)):
        raise TypeError("First name must be a string")
    return(f"Names: {first_name} {last_name}")

#say_my_name('David', 'Ngure')






