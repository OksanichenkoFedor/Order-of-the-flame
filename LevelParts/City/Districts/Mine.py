from Draws.CityDraws import *
from LevelParts.City.Districts.District import *
from Const.City import *


class Mine(District):
    """

    Class of district "Mine"

    : method __init__(side, x, y): Initialise Mine
    : method update(screen): Update district and redraw it

    """
    def __init__(self, side, x, y):
        super().__init__(side, MineLife, x, y, MineNumber)

    def update(self, screen):
        """

        :param screen: Surface, where the picture is rendered

        """
        mine_draw(self, self.side[0], screen)