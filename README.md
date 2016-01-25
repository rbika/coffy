Coffy
=====
Coffy is an nice and fair office tool that makes a lot easier the decision of
who is going to make the coffee. Just give it a list of names and it will
choose one.

Usage
-----
**coffy** [names]

How it works
------------

The ratio (number of times chosen / number of times participated) is used to determine who is going to make the coffee. The one with the lowest ratio will be chosen. If a draw occur, one of the guys will be chosen randomly. 

Installation
------------
For OS X users:

    sudo curl -o /usr/local/bin/coffy https://raw.github.com/rbika/coffy/master/coffy.py
    sudo chmod +x /usr/local/bin/coffy

For Linux users:

    sudo wget -O /usr/local/bin/coffy https://raw.github.com/rbika/coffy/master/coffy.py
    sudo chmod +x /usr/local/bin/coffy

Example
-------
running

    coffy bika rafa wlad dudu mattar

will produce for example:

             ((((
            ((((
             ))))
          _ .---.
         | |`---'|        Wlad
          \|     |        Wed, 01:38 PM
          : .___, :
           `-----´
