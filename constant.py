#--
# Version: 0.1(27-Mar-2017)
# Author: Thomas LEE
# Edited by: Thomas LEE
#--

#--
# Constant object that store all the constant for the program
#--
class Constant(object):
    #--
    # Config for generator
    #--
    GENERATE_CONF = {

        #--
        # Tuple of distribution of number of tickets (mean, sd). 
        #--
        'ticket_distribution': (500, 100),

        #--
        # Ticket price distribution
        # A list of tuples of (mean, sd) of ticket price.
        # The number of items must be align with price_split
        #--
        'ticket_price_distribution': [
            (40, 5),
            (80, 7),
            (100, 9)
        ],

        #--
        # Proporation of tickets in single event
        # A list contains the proporation of count of tickets in different price.
        # It has to be add up to 1.
        # The number of items must be align with price price_distribution
        #--
        'ticket_price_split': [
            0.5,
            0.3,
            0.2
        ],

        #--
        # The boundaries of grid world.
        #--
        'grid_boundaries': {
            'x_max': 10,
            'x_min': -10,
            'y_max': 10,
            'y_min': -10
        },

        #--
        # The density of event. (i.e. How many grids are occupied by a event)
        #--
        'event_density': 0.7
    }

    #--
    # Data folder name
    #--
    DATA_PATH = 'csv_data'

    #--
    # Data file name
    #--
    DATA_FILE = 'data.csv'

    #--
    # Gird config
    #--
    GRID_CONF = {
        'data_path': '/'.join([DATA_PATH, DATA_FILE]),
        'grid_boundaries': GENERATE_CONF['grid_boundaries']
    }
    