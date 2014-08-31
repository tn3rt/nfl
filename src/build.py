__author__ = 'adonis'


from nfl.importer.teams import build_teams
from nfl.importer.plays import build_plays
from nfl.importer.games import build_games
from mongoengine import connect


connect('nfl')
build_teams()
build_plays()
build_games()