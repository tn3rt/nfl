from mongoengine import Document, StringField, SortedListField, IntField, ReferenceField
from nfl.models.games import Game
from nfl.models.teams import Team


class Season(Document):
    team = ReferenceField(Team)
    games = SortedListField(ReferenceField(Game), default=list)
    season = IntField(min_value=1900, max_value=2100, required=True, unique_with=['team'])

    meta = {
        'ordering': ['season']
    }

    def record(self, game_number=22):
        """"Win-Loss-Draw record. Default is final record"""
        win = loss = draw = 0
        up_to = min(len(self.games), game_number)
        for i in range(up_to):
            if self.games[i].winner == self.team:
                win += 1
            elif self.games[i].winner is None:
                draw += 1
            else:
                loss += 1
        return win, loss, draw

    def playoffs(self):
        """Did we make the playoffs?"""
        return len(self.games) > 16

    def __repr__(self):
        def pprint(tag, value):
            return str(tag) + ':\t' + str(value) + '\n'
        string = ''
        string += pprint('team', self.team)
        string += pprint('season', self.season)
        return string

