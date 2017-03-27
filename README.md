# 0. Program environment
Python version: 2.7
Library dependencies:
- numpy
- pandas

# 1. Config the generator
```python
# From constant.py...
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
```

# 2. To generate dataset
```python
python generate_event.py
```

# 3. To run the query program
```python
python query_event.py
```

# 4. Assumption
- random variables are come from normal distribution
- When two events share the same distance, the one with larger event_id will have higher priority
- When a event is running out of tickets, the second cloest event will be replaced

# 5. Questions

## How might you change your program if you needed to support multiple events at the same location?
- the event generator has to be rewrite
- while we are generating the mask for location of events, we use int instead of boolean because each position could have more than one events
- then for every position that contains a number larger than zero, we generate tuples of position according to the number in the mask
- other parts of the program doesn't have to be changed

## How would you change your program if you were working with a much larger world size?
- world size is flexible in the program, but if the world size change, it has to be configed in the constant.py
