from math import sqrt


class Map:
    """

    Class of level Map
    :field x: First coordinate of left up corner of map
    :field y: Second coordinate of left up corner of map
    :field width: Width of picture of map
    :field height: Height of picture of map
    :field number_of_left_roads: Number of left roads
    :field Left_Roads: Massive of left roads, each road has number of tuple, which contains coordinates of nodes of road
    :field number_of_right_roads: Number of right roads
    :field Right_Roads: Massive of right roads, each road has number of tuple, which contains coordinates of nodes of road
    :field Pole_Points: Massive of point of battle pole
    :field self.total_length_L: Massive of full length of each left road
    :field self.total_length_R: Massive of full length of each right road
    :field self.total_coords_L: Massive of coordinate of each node on its road. For left roads
                                First argument - number of road
                                Second argument - number of node
    :field self.total_coords_R: Massive of coordinate of each node on its road. For right roads
                                First argument - number of road
                                Second argument - number of node
    :field bush: Picture of bush
    "field tree: Picture of tree

    :method __init__: Initialise level map. Receives file_name, x, y, w, h

    """

    # TODO Создать класс, который будет по файлу строить карту, а так же её рисовать
    def __init__(self, file_name, x, y, w, h, bush, tree, bushes, trees):
        """

        :param file_name: Name of the file where we will get information about the map
        :param x: First coordinate of left up corner of map
        :param y: Second coordinate of left up corner of map
        :param w: Width of picture of map
        :param h: Height of picture of map


        """
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.bush = bush
        self.tree = tree
        self.trees = trees
        self.bushes = bushes
        file_obj = open(file_name, "r")

        self.number_of_left_roads = int(file_obj.readline())
        self.number_of_right_roads = int(file_obj.readline())
        self.Left_Roads = []
        self.Right_Roads = []
        self.Pole_Points = []
        for i in range(self.number_of_left_roads):
            self.Left_Roads.append([])
            points_number = int(file_obj.readline())
            for j in range(points_number):
                self.Left_Roads[i].append((int(file_obj.readline()) + int(x), int(file_obj.readline()) + int(y)))
        for i in range(self.number_of_right_roads):
            self.Right_Roads.append([])
            points_number = int(file_obj.readline())
            for j in range(points_number):
                self.Right_Roads[i].append((int(file_obj.readline()) + int(x), int(file_obj.readline()) + int(y)))
        self.polygon_points_number = int(file_obj.readline())
        for i in range(self.polygon_points_number):
            self.Pole_Points.append((int(file_obj.readline()) + int(x), int(file_obj.readline()) + int(y)))

        self.total_length_L = []
        self.total_length_R = []
        self.total_coords_L = []
        self.total_coords_R = []

        for i in range(len(self.Left_Roads)):
            self.total_length_L.append(0)
            self.total_coords_L.append([])
            self.total_coords_L[i].append(0)
            for j in range(1, len(self.Left_Roads[i]), 1):
                r = sqrt((self.Left_Roads[i][j][0] - self.Left_Roads[i][j - 1][0]) ** 2 + (
                            self.Left_Roads[i][j][1] - self.Left_Roads[i][j - 1][1]) ** 2)
                self.total_length_L[i] += r
                self.total_coords_L[i].append(self.total_length_L[i])
            for j in range(len(self.Left_Roads[i])):
                self.total_coords_L[i][j] = (1.0 * self.total_coords_L[i][j]) / (1.0 * self.total_length_L[i])

        for i in range(len(self.Right_Roads)):
            self.total_length_R.append(0)
            self.total_coords_R.append([])
            self.total_coords_R[i].append(0)
            for j in range(1, len(self.Right_Roads[i]), 1):
                r = sqrt((self.Right_Roads[i][j][0] - self.Right_Roads[i][j - 1][0]) ** 2 + (
                            self.Right_Roads[i][j][1] - self.Right_Roads[i][j - 1][1]) ** 2)
                self.total_length_R[i] += r
                self.total_coords_R[i].append(self.total_length_R[i])
            for j in range(len(self.Right_Roads[i])):
                self.total_coords_R[i][j] = (1.0 * self.total_coords_R[i][j]) / (1.0 * self.total_length_R[i])

    def nearest_road(self, x, y, side_param):    #Получает на вход координаты x,y и сторона города, из которого вышел юнит
        nearest_road_num = 0
        if side_param == "right":
            distance = ((x-self.Left_Roads[0][-1][0])**2 + (y-self.Left_Roads[0][-1][1])**2)**0.5
            for i in range(len(self.Left_Roads)):
                d = ((x-self.Left_Roads[i][-1][0])**2 + (y-self.Left_Roads[i][-1][1])**2)**0.5
                if d < distance:
                    nearest_road_num = i
                    distance = d

        elif side_param == "left":
            distance = ((x - self.Right_Roads[0][-1][0]) ** 2 + (y - self.Right_Roads[0][-1][1]) ** 2) ** 0.5
            for i in range(len(self.Right_Roads)):
                d = ((x - self.Right_Roads[i][-1][0]) ** 2 + (y - self.Right_Roads[i][-1][1]) ** 2) ** 0.5
                if d < distance:
                    nearest_road_num = i
                    distance = d
        return (nearest_road_num, distance)    #На выходе кортеж из номера ближайшей дороги и расстояния до ее крайнего узла

if __name__ == "__main__":
    print("This module is not for direct call!")
