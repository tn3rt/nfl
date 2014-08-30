__author__ = 'adonis'


from nfl.models.plays import Play
from nfl.models.teams import Team
from datetime import date


def build_plays():
    if not Play.objects.count():
        print('No plays in database')
        return
    if not Team.objects.count():
        print('No teams in database')
        return

    # cache teams in dictionary
    teams = {}
    for team in Team.objects():
        teams[team.name] = team

    def parse_team(team_name):
        return teams[team_name]

    def parse_game_id(game_id):
        game_string = game_id.split('_', 1)
        data = game_string[0]
        teams_in_game = game_string[1].split('@')
        d = date(
            year=int(data[:4]),
            month=int(data[4:6]),
            day=int(data[6:8])
        )
        away = parse_team(teams_in_game[0])
        home = parse_team(teams_in_game[1])
        return d, home, away

    def parse_description(desc):
        pass
        # TODO: add metadata to plays

    def parse_season(date_of_match):
        offset = 0
        if date_of_match.month < 4:
            offset = -1
        return date_of_match.year + offset

    def cast_int(value, default):
        # None, '', '.B'
        try:
            return int(value)
        except:
            return default

    counter = 0
    for play in Play.objects:
        if not play.gameid:
            print('Deleting empty document ' + str(play.id))
            play.delete()
            continue
        play.min = cast_int(play.min, 60)
        play.sec = cast_int(play.sec, 0)
        play.down = cast_int(play.down, None)
        play.togo = cast_int(play.togo, None)
        play.yardline = cast_int(play.yardline, None)
        play.defscore = cast_int(play.defscore, 0)
        play.offscore = cast_int(play.offscore, 0)
        play.date, play.home, play.away = parse_game_id(play.gameid)
        play.possession = parse_team(play.offense) if play.offense else None
        play.season = cast_int(play.season, parse_season(play.date))
        play.save()
        counter += 1
        if counter % 1000 == 0:
            print('Parsed ' + str(counter) + ' plays')

    print('Parsed ' + str(Play.objects.count()) + ' plays')