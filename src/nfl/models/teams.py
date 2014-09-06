from mongoengine import Document, StringField

AFC_N = (
            ('BAL', 'Baltimore Ravens'),
            ('CIN', 'Cincinnatti Bengals'),
            ('CLE', 'Cleveland Browns'),
            ('PIT', 'Pittsburgh Steelers')
        )

AFC_S = (
            ('HOU', 'Houston Texans'),
            ('IND', 'Indianapolis Colts'),
            ('JAC', 'Jacksonville Jaguars'),
            ('TEN', 'Tennessee Titans')
        )

AFC_E = (
            ('BUF', 'Buffalo Bills'),
            ('MIA', 'Miami Dolphins'),
            ('NE',  'New England Patriots'),
            ('NYJ', 'New York Jets')
        )

AFC_W = (
            ('DEN', 'Denver Broncos'),
            ('KC',  'Kansas City Chiefs'),
            ('OAK', 'Oakland Raiders'),
            ('SD',  'San Diego Chargers')
        )

NFC_N = (
            ('CHI', 'Chicago Bears'),
            ('DET', 'Detroit Lions'),
            ('GB',  'Green Bay Packers'),
            ('MIN', 'Minnesota Vikings')
        )

NFC_S = (
            ('ATL', 'Atlanta Falcons'),
            ('CAR', 'Carolina Panthers'),
            ('NO',  'New Orleans Saints'),
            ('TB',  'Tampa Bay Buccaneers')
        )

NFC_E = (
            ('DAL', 'Dallas Cowboys'),
            ('NYG', 'New York Giants'),
            ('PHI', 'Philadelphia Eagles'),
            ('WAS', 'Washington Redskins')
        )

NFC_W = (
            ('ARI', 'Arizona Cardinals'),
            ('SF',  'San Francisco 49ers'),
            ('SEA', 'Seattle Seahawks'),
            ('STL', 'St. Louis Rams')
        )

PB = (
        ('AFC', 'American Football Conference'),
        ('NFC', 'National Football Conference')
     )

AFC = AFC_N + AFC_S + AFC_E + AFC_W
NFC = NFC_N + NFC_S + NFC_E + NFC_W

TEAMS = AFC + NFC + PB


class Team(Document):
    conference = StringField(max_length=3, choices=('AFC', 'NFC'), required=True)
    division = StringField(max_length=1, choices=('N', 'S', 'E', 'W', 'P'), required=True)
    name = StringField(max_length=3, choices=TEAMS, required=True, unique=True)

    def __repr__(self):
        def pprint(tag, value):
            return str(tag) + ':\t' + str(value) + '\n'
        string = ''
        string += pprint('conference', self.conference)
        string += pprint('division', self.division)
        string += pprint('name', self.name)
        return string