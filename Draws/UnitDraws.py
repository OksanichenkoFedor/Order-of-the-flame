from LevelParts.Level import *
from Const.Level import *
from pygame.draw import *


def massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append(int(j[i]*a))
    return j1

def lightinfantry_draw(unit, unit_side, unit_position, screen):
    """

    :param unit: Object Swordsman (we use class unit to avoid circle import)
    :param unit_side: Massive, that contains information, which is important for drawing
                      unit_side[0]: String, which say, what type of unit we have: "Order" , "Union"
                      unit_side[1]: A string that tells which side the given city is located on.
                          If side=="left", than this is city, located in the left side of the level
                          If side=="right", than this is city, located in the right side of the level
    :param unit_position: Massive, which contains:
                                             a.) First coordinate of swordsman in level screen
                                             b.) Second coordinate of swordsman in level screen
    :param screen: Surface, where the picture is rendered

    """
    if unit_side[0] == "order":
        if unit_side[1] == "left":
            circle(screen, RED, massive_multiply(unit_position, DrawingCoefficient), int(15*DrawingCoefficient))
        else:
            circle(screen, RED, massive_multiply(unit_position, DrawingCoefficient), int(15*DrawingCoefficient))
    else:
        if unit_side[1] == "left":
            circle(screen, YLW, massive_multiply(unit_position, DrawingCoefficient), int(15*DrawingCoefficient))
        else:
            circle(screen, YLW, massive_multiply(unit_position, DrawingCoefficient), int(15*DrawingCoefficient))


if __name__ == "__main__":
    print("This module is not for direct call!")
