#!/usr/bin/python3
from cowsay import trex
from sys import argv
if len(argv) == 2:
    trex("Hello, " + argv[1])
