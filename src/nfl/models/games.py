from mongoengine import Document, StringField, SortedListField, ReferenceField, IntField, DateTimeField
from nfl.models.teams import Team
from nfl.models.plays import Play
from nfl.utils import pprint


class Game(Document):
    gameid = StringField(max_length=20, required=True, unique=True)
    home = ReferenceField(Team)
    away = ReferenceField(Team)
    plays = SortedListField(ReferenceField(Play), default=list)
    date = DateTimeField()
    season = IntField(min_value=1900, max_value=2100, required=True)

    meta = {
        'ordering': ['date']
    }

    def score(self, play=-1):
        """Score at a particular play, default final"""
        return self.plays[play].home_score, self.plays[play].away_score

    @property
    def winner(self):
        home_score, away_score = self.score()
        if home_score == away_score:
            return None
        if home_score > away_score:
            return self.home
        else:
            return self.away

    def quarter(self, qtr):
        """Returns 0-indexed play number of first play of quarter"""
        pass
        # TODO: Implement quarter marker

    def __repr__(self):
        string = ''
        string += pprint('gameid', self.gameid)
        string += pprint('date', self.date)
        string += pprint('season', self.season)
        return string