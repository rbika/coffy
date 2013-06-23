#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor:    Rafael Bika
# Email:    rbmbika@gmail.com
# Twitter:  rbika

import os
import sys
import time
import random
import pickle
import datetime

# Globals. {{{
_VERSION = 'Version: 1.1.1'

_ERROR1 = '''Usage: coffy [option] name name [name ...]

Error: Enter at least 2 names.'''

_ERROR2 = 'No statistics stored yet.'

_HELP = '''Usage: coffy [options] action

A simple tool to decide who is going to make the coffee.

Supported actions:
name name [name ...]    list of names to be chosen
help                    display this help message
version                 display version
stats                   display usage statistics
reset                   reset statistics

Options:
-x, --no-stats          does not compute statistics'''


_RESULT = '''
             ((((
            ((((
             ))))
          _ .---.
         | |`---'|        %s
          \|     |        %s
           |     |
          : .___, :
           `-----´
'''

_STATISTICS_PATH = os.path.expanduser('~') + '/.coffy.pkl'
# }}}


def display_result(cguy):
    # Suspense.
    for i in range(3):
        print '.'
        time.sleep(0.8)

    now = datetime.datetime.now()

    print _RESULT % (cguy.capitalize(), now.strftime('%a, %I:%M %p'))


def compute_statistics(cguy):
    def _update(name):
        if name not in data:
            data[name] = {'participated': 0, 'chosen': 0, 'ratio': 0.0}

        if name == cguy:
            data[cguy]['chosen'] += 1

        data[name]['participated'] += 1
        data[name]['ratio'] = float(data[name]['chosen'])
        data[name]['ratio'] /= float(data[name]['participated'])

    try:
        pkl = open(_STATISTICS_PATH, 'r')

    except IOError:
        data = {}

        for name in sys.argv[1:]:
            data[name] = {'participated': 0, 'chosen': 0, 'ratio': 0.0}

    else:
        data = pickle.load(pkl)

        pkl.close()

    pkl = open(_STATISTICS_PATH, 'w')

    map(_update, sys.argv[1:])

    pickle.dump(data, pkl)

    pkl.close()


def display_statistics(data):
    wid1 = max(map(lambda x: len(x), data.keys()))
    wid2 = max(map(lambda x: len(str(x['participated'])), data.values()))
    wid3 = max(map(lambda x: len(str(x['chosen'])), data.values()))
    line = '{:{w1}} participated: {:{w2}}, chosen: {:{w3}}, ratio: {:4.2f}'
    width = {'w1': wid1, 'w2': wid2, 'w3': wid3}
    sdata = sorted(data.items(), key=lambda x: x[1]['ratio'], reverse=True)

    for key, value in sdata:
        val1 = value['participated']
        val2 = value['chosen']
        val3 = value['ratio']

        print line.format(key, val1, val2, val3, **width)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'help':
        print _HELP

    elif len(sys.argv) > 1 and sys.argv[1] == 'version':
        print _VERSION

    elif len(sys.argv) > 1 and sys.argv[1] == 'stats':
        try:
            pkl = open(_STATISTICS_PATH, 'r')

        except IOError:
            print _ERROR2

        else:
            display_statistics(pickle.load(pkl))

            pkl.close()

    elif len(sys.argv) > 1 and sys.argv[1] == 'reset':
        try:
            os.remove(_STATISTICS_PATH)

            print 'statistics erased!'

        except OSError:
            print _ERROR2

    elif len(sys.argv) <= 2:
        print _ERROR1

    else:
        comp_statistics = True

        if sys.argv[1] in ['-x', '--no-stats']:
            comp_statistics = False

        cguy = random.choice(sys.argv[2:])

        display_result(cguy)

        if comp_statistics:
            compute_statistics(cguy)

        else:
            print 'No statistics was computed this time.'

# vim:foldmethod=marker
