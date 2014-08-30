from mongoengine import Document, StringField, IntField
from mongoengine import ListField, BooleanField, ReferenceField, DateTimeField, SortedListField
from nfl.models.teams import Team


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
        pass

    @property
    def away_score(self):
        pass