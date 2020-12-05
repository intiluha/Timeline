# imports

import pandas as pd
import numpy as np
import random

# read table

df = pd.read_csv('data.csv', index_col='Name')[['Date']]

# main loop

events = list(df.index)
random.shuffle(events)
timeline = events[:1]

for event in events[1:]:
    print('The current timeline is:')
    print('()\t'.join(timeline))
    choice = int(input(f'Where woild you put "{event}" on this timeline? \
(type number from 0 to {len(timeline)}) '))
    
    lower_bound = len(df[df.index.isin(timeline) & df['Date'].lt(df.at[event, 'Date'])])
    upper_bound = len(df[df.index.isin(timeline) & df['Date'].le(df.at[event, 'Date'])])
    if lower_bound <= choice <= upper_bound:
        print(f'Correct! {event} happened in {df.at[event, "Date"]}.')
        timeline = timeline[:choice] + [event] + timeline[choice:]
    else:
        print(f'Wrong! {event} happened in {df.at[event, "Date"]}.')
        break
else:
    print('Gratz! You won!')

