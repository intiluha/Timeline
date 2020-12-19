from base import *
import pygame
from typing import List, Tuple, Dict


class Game:
    def __init__(self):
        pass

    def draw_timeline(self, y: int) -> None:
        pass

    def is_timeline_clicked(self, y: int) -> int:
        pass

    def try_put_card(self, y: int) -> bool:
        pass

    def draw_player_hand(self, y: int) -> None:
        pass

    def is_player_hand_clicked(self, y: int) -> int:
        pass

    def draw_results(self, y: int) -> None:
        pass

    def draw_zoomed_in_card(self, card: Card, x: int, y: int) -> None:
        pass

    def shuffle(self) -> None:
        pass

    def start(self) -> None:
        pass

    def pregame(self) -> None:
        pass

    def game(self) -> None:
        pass

    def postgame(self) -> None:
        pass


def can_put_card(card: int, timeline: List[int], position: int, cards: List[Card]) -> bool:
    if position == 0:
        return cards[card].year <= cards[timeline[position]].year
    elif position == len(timeline):
        return cards[timeline[position - 1]].year <= cards[card].year
    else:
        return cards[timeline[position - 1]].year <= cards[card].year <= cards[timeline[position]].year
    # lower_bound = float('-inf') if position == 0 else cards[timeline[position - 1]].date
    # upper_bound = float('inf') if position == len(timeline) else cards[timeline[position]].date
    # return lower_bound <= cards[card].date <= upper_bound


def game(screen: pygame.Surface, players: List[str], permadeath: bool,
         n_cards: int, cards: List[Card]) -> Tuple[Dict[str, int], List[int]]:
    # arrangement params
    screen_w, screen_h = screen.get_width(), screen.get_height()
    card_w, card_h = cards[0].image.get_width(), cards[0].image.get_height()
    name_offset, date_offset, note_offset = -40, card_h + 10, card_h + 50
    player_name_font = pygame.font.SysFont('Tahoma', 60, True, False)
    title_font = pygame.font.SysFont('Tahoma', 30, True, False)
    year_font = pygame.font.SysFont('Tahoma', 30, True, False)
    note_font = pygame.font.SysFont('Tahoma', 12, False, True)

    # set up game
    # TODO change from card indexes to cards themselves
    timeline = [0]
    scores = {p: 0 for p in players}
    # TODO linked list instead of alive and queue
    alive = players[:]
    queue = players[:]
    # deal cards
    # TODO class for player
    player_cards = {p: list(range(n_cards * i + 1, n_cards * (i + 1) + 1)) for i, p in enumerate(players)}
    # TODO object for deck
    top_card = len(players) * n_cards + 1

    # TODO remove selected, rename selected_card to selected
    selected = 0
    selected_card = player_cards[queue[0]][selected]
    while True:
        screen.fill((255, 255, 255))

        # TODO write current player name
        player_name = player_name_font.render(queue[0], True, (0, 0, 0))
        screen.blit(player_name, (0, 0))
        # draw timeline
        for i, j in enumerate(timeline):
            # compute coordinates of top left corner of picture
            coords = (0.5 * screen_w + (2 * i - len(timeline) + 0.5) * card_w, 0.2 * screen_h)
            # draw picture
            screen.blit(cards[j].image, coords)
            # render text to draw next to picture
            title = title_font.render(cards[j].title, True, (0, 0, 0))
            year = year_font.render(str(cards[j].year), True, (0, 0, 0))
            note = note_font.render(cards[j].note, True, (0, 0, 0))
            # draw text
            # TODO align better
            screen.blit(title, (coords[0], coords[1] + name_offset))
            screen.blit(year, (coords[0], coords[1] + date_offset))
            screen.blit(note, (coords[0], coords[1] + note_offset))

        # draw fillers
        for i in range(len(timeline) + 1):
            coords = (0.5 * screen_w + (2 * i - len(timeline) - 0.5) * card_w, 0.2 * screen_h)
            pygame.draw.rect(screen, (200, 200, 0), pygame.Rect(*coords, card_w, card_h))

        # draw players' card(s)
        for i, j in enumerate(player_cards[queue[0]]):
            # compute coordinates of top left corner of picture
            coords = (0.5 * screen_w + (2 * i - len(player_cards[queue[0]]) + 0.5) * card_w, 0.6 * screen_h)
            # draw picture
            screen.blit(cards[j].image, coords)
            # draw text
            # TODO align better
            title = title_font.render(cards[j].title, True, (0, 0, 0))
            screen.blit(title, (coords[0], coords[1] + name_offset))
            # TODO show disambiguation for selected card

        # update the screen
        pygame.display.update()

        # event handling, gets all events from the event queue
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                raise SystemExit
            # TODO scroll timeline
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # process timeline clicks
                # TODO function for processing click
                x, y = event.pos
                if 0.2 * screen.get_height() <= y <= 0.2 * screen.get_height() + card_h:
                    left_border = 0.5 * screen.get_width() - (len(timeline) + 0.5) * card_w
                    for i in range(len(timeline) + 1):
                        if left_border <= x <= left_border + card_w:
                            if can_put_card(selected_card, timeline, i, cards):
                                timeline = timeline[:i] + [selected_card] + timeline[i:]
                                scores[queue[0]] += 1
                                player_cards[queue[0]].pop(selected)
                                if permadeath:
                                    player_cards[queue[0]].append(top_card)
                                    top_card += 1
                                elif not player_cards[queue[0]]:
                                    alive.remove(queue[0])
                                    print(f'{queue[0]} won!')
                                    if not alive:
                                        return scores, timeline
                            else:
                                # TODO show info about failed card
                                if permadeath:
                                    alive.pop(alive.index(queue[0]))
                                    print(f'{queue[0]} lost!')
                                    if not alive:
                                        return scores, timeline
                                else:
                                    player_cards[queue[0]].append(top_card)
                                    top_card += 1
                            queue.pop(0)
                            if not queue:
                                queue = alive[:]
                            selected = 0
                            selected_card = player_cards[queue[0]][selected]
                            break
                        left_border += 2 * card_w

                # TODO allow selection of cards in hand
