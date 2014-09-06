from nfl.models.plays import Play
from nfl.models.games import Game


def build_games():
    if Game.objects.count():
        print('Already loaded games')
        return

    game_ids = Play.objects.distinct('gameid')
    counter = 0
    for game_id in game_ids:
        if not game_id:
            continue
        plays = Play.objects.filter(gameid=game_id).order_by('clock')
        game = Game(
            gameid=game_id,
            home=plays[0].home,
            away=plays[0].away,
            season=plays[0].season,
            date=plays[0].date
        )
        game.save()
        for play in plays:
            game.update(push__plays=play)
        if plays.count() < 50:
            print('Game has less than 50 plays')
            print(game.__repr__())
        counter += 1
        if counter % 25 == 0:
            print('Added ' + str(counter) + ' games')
