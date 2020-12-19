from base import *
import pygame
from typing import List, Tuple


def pregame(surface: pygame.Surface) -> Tuple[List['str'], bool, int, List['str']]:
    # TODO mode selection, player names, tags selection
    players = ['Forever Alone']
    permadeath = True
    n_cards = 1
    tags = ['inventions', 'PL']
    return players, permadeath, n_cards, tags
