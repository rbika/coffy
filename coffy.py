#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: Coffy
# Version: 2.0
# Author: Rafael Bika

import os
import sys
import random
import sqlite3
import datetime

# Globals. {{{
_DATABASE_PATH = os.path.expanduser('~') + '/.coffy.db'

_ERROR1 = 'Enter at least one name.'

_RESULT = u'''
      ((((
     ((((
      ))))
   _ .---.
  | |`---'|      %s
   \|     |      %s
   : .___, :
    `-----´
'''
# }}}


class User(object):
    def __init__(self, name, chosen, participated):
        self.name = name
        self.chosen = chosen
        self.participated = participated
        self.ratio = float(chosen) / float(participated) if participated else 0

    def print_stats(self):
        data = (self.name, self.chosen, self.participated, self.ratio)

        print('%s - chosen: %d, participated: %d, %.2f' % data)


class Coffy(object):
    def __init__(self, names):
        self.date = datetime.datetime.now()
        self.participants = []
        self.chosen_user = ''

        cur.execute('''CREATE TABLE IF NOT EXISTS User (id TEXT PRIMARY KEY,
            chosen INT, participated INT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Log (id INT PRIMARY KEY,
            chosen_user TEXT, date DATETIME)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS UserLog (id INT PRIMARY KEY,
            UserId TEXT, LogId INT)''')

        for name in names:
            query = u'SELECT * FROM User WHERE Id=?'
            data = cur.execute(query, (name,)).fetchone()

            if not data:
                data = (name, 0, 0)

            self.participants.append(User(*data))

    def choose(self):
        ratio = 1
        lst = []

        for user in self.participants:
            if user.ratio == ratio:
                lst.append(user)

            elif user.ratio < ratio:
                ratio = user.ratio
                lst = [user]

        if len(lst) == 1:
            self.chosen = lst[0].name

        elif len(lst) > 1:
            self.chosen = random.choice(lst).name

        for user in self.participants:
            if user.name == self.chosen:
                user.chosen += 1

            user.participated += 1
            user.ratio = float(user.chosen) / float(user.participated)

    def print_stats(self):
        for user in self.participants:
            user.print_stats()

    def print_result(self):
        print(_RESULT % (self.chosen, self.date.strftime('%a, %I:%M %p')))

    def save(self):
        cnt1 = cur.execute('SELECT COUNT (id) FROM UserLog').fetchone()[0] + 1
        cnt2 = cur.execute('SELECT COUNT (id) FROM Log').fetchone()[0] + 1

        for user in self.participants:
            data = (user.chosen, user.participated, user.name)

            cur.execute('INSERT OR IGNORE INTO User VALUES (?, 0, 0)',
                (user.name,))

            cur.execute('''UPDATE User SET chosen=?, participated=?
                WHERE id=?''', data)

            cur.execute('INSERT INTO UserLog VALUES (?, ?, ?)',
                (cnt1, user.name, cnt2))

            cnt1 += 1

        cur.execute('INSERT INTO Log VALUES (?, ?, ?)',
            (cnt2, self.chosen, self.date))

        con.commit()


if __name__ == '__main__':
    con = sqlite3.connect(_DATABASE_PATH)

    with con:
        cur = con.cursor()

        if sys.argv[1:]:
            coffy = Coffy(sys.argv[1:])

            coffy.print_stats()
            coffy.choose()
            coffy.print_result()
            coffy.save()

        else:
            print _ERROR1

# vim:foldmethod=marker
