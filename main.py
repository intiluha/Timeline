# import the pygame module, so you can use it
from base import *
from random import shuffle
from pregame import *
from game import *
from postgame import *
# TODO all card images should be made the same size


def init(tags: List[str]) -> List[Card]:
    # TODO tags matching
    with open('cards.csv', newline='') as f:
        f.readline()
        reader = csv.reader(f)
        cards = [Card(pygame.image.load(os.path.join('img', row[0] + '.png')), *row[1:5]) for row in reader]
    return cards


# initialize the pygame module
pygame.init()

# load and set the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

# set caption
pygame.display.set_caption("Timeline")

# create a surface on screen
screen = pygame.display.set_mode((0, 0))

restart = False
try:
    while True:
        if not restart:
            # choose game mode
            players, permadeath, n_cards, tags = pregame(screen)
            # init cards
            cards = init(tags)
        shuffle(cards)
        shuffle(players)
        scores, timeline = game(screen, players, permadeath, n_cards, cards)
        restart = postgame(screen, scores, timeline, cards)
except SystemExit:
    pygame.quit()
