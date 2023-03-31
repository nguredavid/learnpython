#!/usr/bin/python3

#Write a function that prints an integer with

def safe_print_integer(value):
    try:
        print(f' {value}')
        return True
    except Exception:
        return False

val = 89

safe_print_integer(val)
