#!/usr/bin/python3
from cowsay import cow
from sys import argv
if len(argv) == 2:
    cow("Hello, " + argv[1])
