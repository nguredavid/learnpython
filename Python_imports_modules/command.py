#!/usr/bin/python3
import cowsay
from cowsay import trex
from sys import argv
if len(argv) == 2:
    trex("Hello, " + argv[1])
print(dir(cowsay))
