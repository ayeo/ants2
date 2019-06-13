import math
import random
import numpy as np

class Ant():
    breadcrumb = []
    carrying = False

    def __init__(self, id, position, board_size):
        self.id = id
        self.step = 0
        self.position = position
        self.angle = random.randint(0, 360)
        self.new_angle = self.angle
        self.speed = 3
        self.sense = 7
        self.board_size = board_size
        self.pheromones = np.full((board_size, board_size), 0.0, dtype=float)

    def leave_pheromone(self, quantity):
        self.pheromones[self.position] = self.pheromones[self.position] + quantity

    def get_position(self, pheromones, x, y):
        ppp = pheromones - self.pheromones
        for last in self.breadcrumb:
            ppp[last] = 0

        slice = np.array(ppp[y, x])
        center = int((self.sense - 1) / 2)
        if slice.size == 0:
            return None

        slice[center, center] = 0
        max = 0
        cell = (-1, -1)
        for y, column in enumerate(slice):
            for x, value in enumerate(column):
                if (value > max):
                    cell = (y, x)
                    max = value

        if cell == (-1, -1) :
            return None
        else:
            t = tuple(np.array(cell) - [center, center])
            return t

    def update(self, pheromones):
        distance = (self.sense - 1) / 2
        position = self.position
        y = slice(int(position[0] - distance), int(position[0] + distance + 1))
        x = slice(int(position[1] - distance), int(position[1] + distance + 1))
        fixed_position = self.get_position(pheromones, x, y)

        if fixed_position:
            z = tuple(np.array(self.position) + np.array(list(fixed_position)))
            angle = math.atan2(self.position[0] - z[0], self.position[1] - z[1])
            self.angle = math.degrees(angle) + 90

            self.position = z
            self.breadcrumb.append(self.position)
            self.breadcrumb = self.breadcrumb[-100:]




        else:
            if self.angle == self.new_angle:
                if random.randint(0, 10) == 4:
                    self.new_angle = self.angle - random.randint(-180, 180)
            else:
                x = (self.angle - self.new_angle) / 3
                if math.fabs(x) < 1:
                    self.angle = self.new_angle
                else:
                    self.angle = self.angle - x

            theta = self.angle * math.pi / 180
            delta_x = self.speed * math.cos(theta)
            delta_y = self.speed * math.sin(theta)
            new_position = (int(self.position[0] + delta_x), int(self.position[1] + delta_y))

            if new_position[1] < 0 or new_position[1] >= self.board_size:
                self.angle = round(360 - self.angle, 2)
                self.new_angle = round(360 - self.new_angle, 2)
                return

            if new_position[0] < 0 or new_position[0] >= self.board_size:
                self.angle = round(360 - self.angle + 90, 2)
                self.new_angle = round(360 - self.new_angle + 90, 2)
                return

            self.position = new_position