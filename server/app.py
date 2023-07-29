#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if not animal:
        return 'Does not exist', 404
    response = f'<ul>Name: {animal.name}</ul>'
    response += f'<ul>Species: {animal.species}</ul>'
    response += f'<ul>Zookeeper: {animal.zookeeper}</ul>'
    response += f'<ul>Enclosure: {animal.enclosure}</ul>'
    return response, 200

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    if not zookeeper:
        return 'Does not exist', 404
    response = f'<ul>Name: {zookeeper.name}</ul>'
    response += f'<ul>Birthday: {zookeeper.birthday}</ul>'
    for animal in zookeeper.animals:
        response += f'<ul>Animal: {animal}</ul>'
    return response, 200

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    if not enclosure:
        return 'Does not exist', 404
    
    response = f'<ul>Environment: {enclosure.environment}</ul>'
    response += f'<ul>Open to Visitors: {str(enclosure.open_to_visitors)}</ul>'
    for animal in enclosure.animals:
        response += f'<ul>Animal: {animal}</ul>'

    return response, 200
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
