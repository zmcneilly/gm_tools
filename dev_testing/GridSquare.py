"""
This library is a single class, the GridSquare class which tracks Grid Squares
"""
from PIL import Image
import uuid

class GridSquare(object):
    """
    This class defines a grid square.
    Each grid square should have:
        - A type
        - A dict of 4 neighbors
        - An UUID as an id
    """
    # Types is a dict with the name of a type as the index and an image as the
    # value. The idea is that it should be easy to draw the same image multiple
    # times on another image.
    types = {
        'empty': None,
        'creature': Image.open('flame.jpeg', 'r'),\
        'trap': Image.open('trap.gif', 'r'),\
        'feature': Image.open('feature.png', 'r'),\
        'wall': Image.open('wall.png', 'r')\
    }
    default_group = {'North': None,\
            'East': None,\
            'South': None,\
            'West': None}

    def __init__(self, fill=None, neighbors=None):
        """
        This is the constructor for a grid square. It defaults to creating all
        empty values.
        """
        if fill == None:
            fill = 'empty'
        elif fill not in GridSquare.types.keys():
            raise KeyError(fill)

        self.fill = GridSquare.types[fill]

        if neighbors == None:
            neighbors = dict(GridSquare.default_group)
        elif type(neighbors) != type({}):
            raise TypeError('neighbors must be a dictionary')

        self.neighbors = neighbors

        self.ident = str(uuid.uuid4())

    def set_neighbor(self, square_id, direction):
        """
        This method assigns an id that links this square to the square in a
        direction.
        """
        if direction not in self.neighbors.keys():
            raise KeyError(direction)
        elif type(square_id) != type(""):
            raise TypeError('square_id must be an UUID as a string')

        self.neighbors[direction] = square_id

    def get_neighbor(self, direction):
        """
        This method returns the neighbor in the specified direction
        """
        if direction not in self.neighbors.keys():
            raise KeyError(direction)

        return self.neighbors[direction]

    def set_fill(self, fill):
        """
        This method sets the fill for a square
        """
        if fill not in GridSquare.types.keys():
            raise KeyError(fill)

        self.fill = GridSquare.types[fill]

    def get_fill(self):
        """
        This method returns the name of the type
        """
        return self.fill

    def get_id(self):
        """
        This method returns the uuid of this square
        """
        return self.ident
