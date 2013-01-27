#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor:    Rafael Bika
# Email:    rbmbika@gmail.com
# Twitter:  rbika

# Python imports.
import sys
import time
import random

# Messages.
_VERSION = 'Version: 1.0'

_ERROR = '''Usage: coffy [-h] [-v] name name [name ...]

Error: Enter at least 2 names.'''

_HELP = '''Usage: coffer [-h] [-v] name name [name ...]

Description: A simple tool to decide who is going to make the coffee.

Positional arguments:
name            a guy to be chosen.

Optional arguments:
-h, --help      display this help message.
-v, --version   display version.'''

def suspense():
    for i in range(3):
        print '.'
        time.sleep(1.5)

def choose(lst):
    msg = '''
             ((((
            ((((
             ))))
          _ .---.
         ( |`---'|        %s
          \|     |
          : .___, :
           `-----´
    '''

    print msg % random.choice(lst).capitalize()

if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']:
    print _HELP

elif len(sys.argv) > 1 and sys.argv[1] in ['--version', '-v']:
    print _VERSION

elif len(sys.argv) <= 2:
    print _ERROR

else:
    suspense()
    choose(sys.argv[1:])
