from mongoengine import *

connect('nfl')

class Play(Document):
    description = StringField(required=True)

    offense = StringField(required=True)
    defense = StringField(required=True)

    down = IntField()
    togo = IntField()
    ydline = IntField()

    qtr = IntField(min_value=1, required=True)
    minutes = IntField()
    seconds = IntField()

    offscore = IntField(min_value=0, required=True)
    defscore = IntField(min_value=0, required=True)

    gameid = StringField(required=True)
    season = IntField(required=True)

    scorechange = IntField()
    nextscore = IntField()
    scorediff = IntField()
    series1stdn = IntField(min_value=0, max_value=1)
    teamwin = IntField(min_value=0, max_value=1)

    meta = {'collection' : 'play' }

for p in Play.objects:
    if p.down == 1:
        print p.description
