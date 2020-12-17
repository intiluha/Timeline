from base import *


def pregame(surface: pygame.Surface) -> Tuple[List['str'], bool, int, List['str']]:
    # TODO mode selection, player names, themes selection
    players = ['Forever Alone']
    permadeath = True
    n_cards = 1
    tags = ['inventions', 'PL']
    return players, permadeath, n_cards, tags


# # get list of all themes
# themes = list_themes()
#
# #
#
# # load card images
# cards = [pygame.image.load(os.path.join('img', 'card.png')).convert()]*10
# button = pygame.Surface((100, 50))
# button.fill(red)
