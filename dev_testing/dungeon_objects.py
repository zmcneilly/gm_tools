from PIL import Image
import uuid

class GridSquare():
    """
    This class defines a grid square.
    Each grid square should have:
        - A type
        - A dict of 4 edges
        - A dict of 4 neighbors
        - An UUID as an id
    """
    # Types is a dict with the name of a type as the index and an image as the
    # value. The idea is that it should be easy to draw the same image multiple
    # times on another image.
    types = {
        'empty': None,
        'creature': Image.open('flame.jpeg','r'),
        'trap': Image.open('trap.gif','r'),
        'feature': Image.open('feature.gif','r'),
    }
    default_group = {'North': None,
            'East': None,
            'South': None,
            'West': None}

    def __init__(self, lines=None, fill=None, neighbors=None):
        """
        This is the constructor for a grid square. It defaults to creating all
        empty values.
        """
        if lines == None:
            lines = dict(default_group)
        self.lines = lines

        if fill == None:
            fill = 'empty'
        self.fill = types[fill]

        if neighbors == None:
            neighbors = dict(default_group)
        self.neighbors = neighbors

        self.ident = str(uuid.uuid4())

