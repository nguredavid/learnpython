#!/usr/bin/python3
from cowsay import pig
from sys import argv
if len(argv) == 2:
    pig("Hello, " + argv[1])
