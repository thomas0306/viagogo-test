#--
# Version: 0.1(27-Mar-2017)
# Author: Thomas LEE
# Edited by: Thomas LEE
#--

import itertools

import numpy as np
import pandas as pd

from constant import Constant as con

#--
# EventGenerator object
# Generator for generating event dataset
# Constructor:
#   event_density: the density of events within the grid
#   grid_boundaries: the boundaries of the grid
#   ticket_distribution: parameters for normal distribution of number of tickets
#   ticket_price_split: the proporation of tickets for different ticket type
#   ticket_price_distribution: the distribution of the price ticket of different ticket type
# Assumption:
#   Random variables are all come from normal distribution
# Recommandation:
#   change the constructor parameters according to constant.py
#--
class EventGenerator(object):
    def __init__(self,
        event_density=0.7,
        grid_boundaries={
            'x_max': 10,
            'x_min': -10,
            'y_max': 10,
            'y_min': -10
        }, 
        ticket_distribution=(500, 100),
        ticket_price_split=[1.0],
        ticket_price_distribution=[(10, 5)]
    ):
        self.dataset = None
        self.ticket_distribution = ticket_distribution
        self.ticket_price_distribution = ticket_price_distribution
        self.ticket_price_split = ticket_price_split
        self.grid_boundaries = grid_boundaries
        self.event_density = event_density
    
    #--
    # Generate a dataset according to the config
    #--
    def generate(self):
        # 1. generate random event grid (mask)
        x_len = abs(self.grid_boundaries['x_max'] - self.grid_boundaries['x_min'])
        y_len = abs(self.grid_boundaries['y_max'] - self.grid_boundaries['x_min'])
        mask = np.random.choice([True, False], size=(y_len, x_len), p=[self.event_density, 1 - self.event_density])
        
        # 2. Find the coordinates with true value
        coordinates = np.argwhere(mask)

        # 3. Fit it into the range given
        x_diff = x_len - max(self.grid_boundaries['x_max'], self.grid_boundaries['x_min'])
        y_diff = y_len - max(self.grid_boundaries['y_max'], self.grid_boundaries['y_min'])
        # * switch back to (x, y) format
        coordinates = [(loc[1] - x_diff, loc[0] - y_diff) for loc in coordinates]

        # 4. Give a event id
        coordinates = [{'event_id': idx + 1, 'location': loc} for idx, loc in enumerate(list(coordinates))]

        # 5. Generate event dataframe
        event_df = pd.concat([self.generate_event(**event) for event in coordinates])

        self.dataset = event_df

    #--
    # Return the dataset hold by the instance
    # return:
    #   a dataframe contains the sample data
    #--
    def get_dataset(self):
        return self.dataset

    def generate_event(self, event_id, location):
        # 1. generate the number of tickets
        number_of_tickets = int(np.random.normal(*self.ticket_distribution))

        # 2. transform proporation of ticket price to exact number
        tickets_count = np.round([number_of_tickets * proporation for proporation in self.ticket_price_split])
        # tuning the last proporation so that it meets the total expected
        tickets_count[-1] -= np.sum(tickets_count) - number_of_tickets

        # 3. Generate tickets according to ticket_distribution
        tickets = list(itertools.chain.from_iterable([np.random.normal(*self.ticket_price_distribution[idx], size=int(cnt)) for idx, cnt in enumerate(list(tickets_count))]))
        
        # 4. Two decimal places for USD
        tickets = [round(p, 2) for p in tickets]

        # 5. Return a dataframe
        return pd.DataFrame({
            'event_id': [event_id for i in range(number_of_tickets)],
            'price': tickets,
            'x': [location[0] for i in range(number_of_tickets)],
            'y': [location[1] for i in range(number_of_tickets)],
        })


if __name__ == "__main__":

    # generate dataset
    generator = EventGenerator(**con.GENERATE_CONF)
    generator.generate()
    df = generator.get_dataset()

    # write dataset
    try:
        df.to_csv('/'.join([con.DATA_PATH, con.DATA_FILE]))
    except IOException as ioe:
        print ioe
