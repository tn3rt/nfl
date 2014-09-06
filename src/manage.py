__author__ = 'adonis'


from mongoengine import connect
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    subparser = parser.add_subparsers(dest='command', help='Options')
    imp = subparser.add_parser('build', help="Import NFL data")
    imp.add_argument('-t', '--teams', action='store_true', help="Import teams data")
    imp.add_argument('-p', '--plays', action='store_true', help="Import plays data")
    imp.add_argument('-g', '--games',  action='store_true',help="Import games data")
    imp.add_argument('-s', '--seasons',  action='store_true',help="Import seasons data")

    shell = subparser.add_parser('shell', help='Start NFL Python shell')

    ns = parser.parse_args()

    connect('nfl')

    if ns.command == 'shell':
        from nfl.models.plays import Play
        from nfl.models.games import Game
        from nfl.models.teams import Team
        from nfl.models.seasons import Season
        print('Starting NFL Shell')
        import code
        vars = globals().copy()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()
    elif ns.command == 'build':
        if not (ns.teams or ns.plays or ns.games or ns.seasons):
            ns.teams = ns.games = ns.plays = ns.seasons = True
        if ns.teams:
            from nfl.importer.teams import build_teams
            print('Loading teams')
            build_teams()
        if ns.plays:
            from nfl.importer.plays import build_plays
            print('Loading plays')
            build_plays()
        if ns.games:
            from nfl.importer.games import build_games
            print('Loading games')
            build_games()
        if ns.seasons:
            from nfl.importer.seasons import build_season
            print('Loading seasons')
            build_season()
    else:
        parser.print_help()

