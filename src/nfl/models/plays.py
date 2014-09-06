from mongoengine import Document, StringField, IntField
from mongoengine import ListField, BooleanField, ReferenceField, DateTimeField, SortedListField
from nfl.models.teams import Team
from nfl.utils import pprint


class Play(Document):
    gameid = StringField(max_length=20, required=True)
    quarter = IntField(db_field='qtr', min_value=1, max_value=6, required=True)
    min = IntField(required=True)
    sec = IntField(required=True)
    home = ReferenceField(Team)
    away = ReferenceField(Team)
    date = DateTimeField()
    offense = StringField(db_field='off', max_length=3)
    defense = StringField(db_field='def', max_length=3)
    possession = ReferenceField(Team)
    possession_change = BooleanField(default=False)
    down = IntField(min_value=1, max_value=4)
    togo = IntField(min_value=0, max_value=100)
    yardline = IntField(db_field='ydline', min_value=0, max_value=120)
    offscore = IntField(min_value=0, max_value=100, required=True)
    defscore = IntField(min_value=0, max_value=100, required=True)
    description = StringField(required=True)
    tags = ListField(StringField(max_length=24), default=list)
    players = ListField(StringField(max_length=24))
    season = IntField(min_value=1900, max_value=2100)

    # meta = {
    #    'indexes': ['season', 'date', 'gameid'],
    #    'ordering': ['season', 'date', 'gameid', 'clock']
    #}

    @property
    def clock(self):
        t = float(self.min) + float(self.sec) / 60
        return 60 - t

    @property
    def home_score(self):
        if self.home.name == self.offense:
            return self.offscore
        else:
            return self.defscore

    @property
    def away_score(self):
        if self.away.name == self.offense:
            return self.offscore
        else:
            return self.defscore

    def __repr__(self):
        string = ''
        string += pprint('id', self.id)
        string += pprint('gameid', self.gameid)
        string += pprint('quarter', self.quarter)
        string += pprint('min', self.min)
        string += pprint('sec', self.sec)
        string += pprint('offense', self.offense)
        string += pprint('defense', self.defense)
        string += pprint('down', self.down)
        string += pprint('togo', self.togo)
        string += pprint('offscore', self.offscore)
        string += pprint('defscore', self.defscore)
        string += pprint('description', self.description)
        string += pprint('season', self.season)
        return string