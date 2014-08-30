__author__ = 'adonis'


from nfl.importer.teams import build_teams
from nfl.importer.plays import build_plays
from mongoengine import connect


connect('nfl')
build_teams()
build_plays()