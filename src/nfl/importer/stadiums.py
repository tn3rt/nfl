__author__ = 'trent'

from nfl.models.stadiums import Stadium
from nfl.models.teams import Team
from datetime import datetime

def build_stadiums():
    if Stadium.objects.count():
        print('Already loaded stadiums')
        return
    '''Buffalo Bills'''
    Stadium(
        name='Ralph Wilson Stadium',
        capacity = 75339,
        dome = False,
        grass = False,
        home = Team.name['BUF'],
        start = datetime.datetime.strptime("1973", "%d-%b-%Y")
    ).save()
    Stadium(
        name='Rogers Centre',
        capacity = 54000,
        dome = False,
        grass = False,
        home = Team.name['BUF'],
        start = datetime.datetime.strptime("2008", "%Y")
    ).save()
    Stadium(
        name='War Memorial Stadium',
        capacity = 46500,
        dome = False,
        grass = True,
        home = Team.name['BUF'],
        start = datetime.datetime.strptime("1960", "%Y"),
        end = datetime.datetime.strptime("1972","%Y")
    ).save()
    '''Miami Dolphins'''
    Stadium(
        name='Sun Life Stadium',
        capacity = 75000,
        dome = False,
        grass = True,
        home = Team.name['MIA'],
        start = datetime.datetime.strptime("1987", "%Y"),
    ).save()
    ''' Need way to enter multiple surfaces '''
    Stadium(
        name='Miami Orange Bowl',
        capacity = 74476,
        dome = False,
        grass = False,
        home = Team.name['MIA'],
        start = datetime.datetime.strptime("1966","%Y"),
        end = datetime.datetime.strptime("1986","%Y")
    )
    