# Python.
from random import choice
from datetime import datetime

# Pymongo.
from pymongo import Connection

# Bottle.
from bottle import route, request, run, template, redirect

db = Connection("mongodb://localhost", safe=True).coffy


@route('/')
def home():
    form_names = request.query.getlist('names')
    context = {'result': ''}

    if len(form_names) > 1:
        now = datetime.now()
        chosen = choice(form_names)
        doc1 = {'names': form_names, 'created': now, 'chosen': chosen}
        doc2 = {'$inc': {'participated': 1}}
        doc3 = {'$inc': {'chosen': 1}}

        db.coffy_log.insert(doc1)
        db.coffy_user.update({'name': {'$in': form_names}}, doc2, multi=True)
        db.coffy_user.update({'name': chosen}, doc3)

        context['result'] = chosen

    context['names'] = [x['name'] for x in db.coffy_user.find()]

    return template('home', **context)


@route('/add')
def add_name():
    name = request.query.get('name', '')

    if name:
        doc = {'name': name, 'participated': 0, 'chosen': 0}

        db.coffy_user.insert(doc)

        redirect('/')


run(host='localhost', port=8080, debug=True, reloader=True)
