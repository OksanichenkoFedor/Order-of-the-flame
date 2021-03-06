from Draws.CityDraws import *
from LevelParts.City.Districts.District import *
from Const.City import *


class CityCentre(District):
    """

    Class of district "City Centre"

    :field image_castle_order: Image of city centre main building
    :field image_castle_square: Image of square

    : method __init__(side, x, y): Initialise City Centre. Do the super()__init__() life = life of city centre.
                                   Receives side, x, y
    : method update(screen): Update district and redraw it

    """
    def __init__(self, side, x, y, image_castle, image_square, image_master):
        super().__init__(side, CityCentreLife, x, y, CityCentreNumber, image_master)
        self.image_castle = image_castle
        self.image_square = image_square
        self.master = 1

    def update(self):
        pass

    def draw(self, screen):
        city_centre_draw(self, screen, self.image_castle, self.image_square, self.image_master)

