Coffee's Guy - coffy
====================
Coffee's Guy is an nice office tool, that makes a lot easier the decision of who is going to make the coffee.
Just give it a list of names and it will choose one.

Usage
-----
**coffy** [options] action

Supported actions
-----------------
	name name [name ...]    list of names to be chosen
	help                    display this help message
	version                 display version
	stats                   display usage statistics
	reset                   reset statistics

Options
-------
    -x, --no-stats     does not compute statistics

Installation
------------
For OS X users:  
`sudo curl -o /opt/local/bin/coffy https://raw.github.com/rbika/coffy/master/coffy.py`  
`sudo chmod +x /opt/local/bin/coffy`  

For Linux users:  
`sudo wget -O /usr/local/bin/coffy https://raw.github.com/rbika/coffy/master/coffy.py`  
`sudo chmod +x /usr/local/bin/coffy`  

Example
-------
running:  
`coffy bika rafa wlad dudu mattar`  

You'll get for example:

             ((((
            ((((
             ))))
          _ .---.
         ( |`---'|        Wlad
          \|     |
          : \___' :
           `-----´
