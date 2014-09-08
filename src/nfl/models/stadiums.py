__author__ = 'trent'

from mongoengine import Document, StringField, DateTimeField, ReferenceField, BooleanField, ListField, IntField
from nfl.models.teams import Team
from nfl.utils import pprint

'''SURFACES = (
    ('g', 'grass'),
    ('atf', 'A-Turf Titan'),
    ('ap', 'AstroPlay'),
    ('at', 'AstroTurf'),
    ('ft', 'FieldTurf'),
    ('pt', 'Poly-Turf'),
    ('smt', 'Sportexe Momentum Turf'),
    ('tt', 'Tartan Turf'),
    ('dg', 'Desso GrassMaster'),
    ('mat', 'Matrix artificial turf'),
    ('rg', 'RealGrass'),
    ('st', 'Superturf'),
    ('ubu', 'UBU-Intensity Series-S5-M Synthetic Turf'),
    ('sf', 'SportField')
)'''

class Stadium(Document):
    name = StringField(required=True)
    capacity = IntField()
    dome = BooleanField(default=False)
    grass = BooleanField(default=True)
    '''surface = StringField(choices=SURFACES)'''
    home = ListField(ReferenceField(Team))
    start = DateTimeField()
    end = DateTimeField(default=None)

    def __repr__(self):
        string = ''
        string += pprint('name', self.name)
        string += pprint('capacity', self.capacity)
        string += pprint('dome', self.dome)
        string += pprint('grass', self.grass)
        for team in self.home:
            string += pprint('home', team.name)
        string += pprint('start', self.start)
        string += pprint('end', self.end)
        return string