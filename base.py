from typing import List
import pygame
import os.path

__all__ = ['Card', 'Player']


class Card:
    def __init__(self, card_id: str, title: str, year: int, disambiguation: str, note: str):
        self.image = pygame.image.load(os.path.join('img', card_id + '.png'))
        self.title = title
        self.year = int(year)
        self.disambiguation = disambiguation
        self.note = note


class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards = []
        self.score = 0

    def draw(self, deck: List[Card], n: int = 1) -> None:
        for _ in range(n):
            self.cards.append(deck.pop())
