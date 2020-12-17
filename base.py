import pygame
import os.path
import csv
from typing import List, Tuple, Dict, Any, TypeVar


class Card:
    def __init__(self, image: pygame.Surface, name: str, date: int, disambiguation: str, note: str):
        self.image = image
        self.name = name
        self.date = int(date)
        self.disambiguation = disambiguation
        self.note = note
        if not isinstance(self.date, int):
            print(f'date for {name} is not an integer ({date})')
