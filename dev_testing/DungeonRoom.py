import GridSquare
import random
from PIL import Image, ImageDraw

class DungeonRoom(object):
    """
    This class is an object which describes a room in the Dungeon. It includes a
    list of GridSquares, creatures, and the top-left position
    """
    def __randint(self, a, b, seed):
        """
        This method is intended only for internal use. It takes three
        arguments:

        a - The smallest number returnable
        b - The largest number returnable
        seed - The random seed to be used
        """
        random.seed(seed)
        r = random.random()
        random.seed()

        return a+int(r*(b-a))

    def __init_grid(self):
        max_row = self.width+1
        max_col = self.height+1
        for row in xrange(0, max_row+1):
            for col in xrange(0, max_col+1):
                if row == 0 or row == max_row or\
                    col == 0 or col == max_col:
                    self.squares[(row,col)] = GridSquare.GridSquare(fill='wall')
                else:
                    self.squares[(row,col)] = GridSquare.GridSquare()

    def draw_grid(self):
        im = Image.new('RGB', ((self.width+2)*20, (self.height+2)*20))
        draw = ImageDraw.Draw(im)
        max_row = self.width+1
        max_col = self.height+1
        for row in xrange(0, max_row+1):
            for col in xrange(0, max_col+1):
                x0 = 20*row
                y0 = 20*col
                x1 = x0+20
                y1 = y0+20

                im.paste(self.squares[(row,col)].get_fill(), \
                    [(x0,y0),(x1,y1)])
                draw.rectangle([(x0,y0),(x1,y1)], outline='teal')

        return im




    def __init__(self, seed, order, max_side, pos): 
       
        rseed = str(seed)+str(order)
        wseed = str(rseed)+"w"
        hseed = str(rseed)+"h"

        self.width = self.__randint(1, max_side, wseed)
        self.height = self.__randint(1, max_side, hseed)

        self.order = order
        self.squares = {}

        self.__init_grid()

