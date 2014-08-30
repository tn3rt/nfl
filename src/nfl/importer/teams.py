from nfl.models.teams import Team
from nfl.models.teams import AFC_E, AFC_W, AFC_N, AFC_S
from nfl.models.teams import NFC_E, NFC_W, NFC_N, NFC_S, PB


def build_teams():
    if Team.objects.count():
        print('Already loaded teams')
        return
    for team, name in AFC_E:
        Team(conference='AFC', division='E', name=team).save()
    for team, name in AFC_W:
        Team(conference='AFC', division='W', name=team).save()
    for team, name in AFC_N:
        Team(conference='AFC', division='N', name=team).save()
    for team, name in AFC_S:
        Team(conference='AFC', division='S', name=team).save()
    for team, name in NFC_E:
        Team(conference='NFC', division='E', name=team).save()
    for team, name in NFC_W:
        Team(conference='NFC', division='W', name=team).save()
    for team, name in NFC_N:
        Team(conference='NFC', division='N', name=team).save()
    for team, name in NFC_S:
        Team(conference='NFC', division='S', name=team).save()
    for team, name in PB:
        Team(conference=team, division='P', name=team).save()
    print('Loaded ' + str(Team.objects.count()) + ' teams')
