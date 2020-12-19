# import the pygame module, so you can use it
import pygame
import csv
from typing import List
from base import *
from random import shuffle
from pregame import pregame
from game import game
from postgame import postgame
# TODO all card images should be made the same size


def init(tags: List[str]) -> List[Card]:
    with open('cards.csv', newline='') as f:
        f.readline()
        reader = csv.reader(f)
        cards = [Card(*row[:5]) for row in reader if row[5] in tags]
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
