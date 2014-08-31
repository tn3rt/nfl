__author__ = 'adonis'


from nfl.models.seasons import Season
from nfl.models.teams import Team
from nfl.models.games import Game
from mongoengine import Q


def build_season():
    if Season.objects.count():
        print('Already loaded seasons')
        return

    seasons = Game.objects.distinct('season')
    for team in Team.objects():
        print("Parsing " + team.name)
        for season in seasons:
            games = Game.objects(Q(home=team) | Q(away=team)).filter(season=season)
            doc = Season(
                team=team,
                season=season
            )
            doc.save()
            for game in games:
                doc.update(push__games=game)