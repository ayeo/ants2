import math
import random

class Ant():
    def __init__(self, id, position, board_size):
        self.id = id
        self.position = position
        self.angle = random.randint(0, 360)
        self.new_angle = self.angle
        self.speed = 10
        self.board_size = board_size

    def update(self, *args):
        if (self.angle == self.new_angle and random.randint(4, 4) == 4):
            self.new_angle = self.angle - random.randint(-180, 180)

        if (self.angle > self.new_angle):
            x = math.fabs(self.angle - self.new_angle) / 2
            if x < 1:
                self.angle = self.new_angle
            else:
                self.angle = self.angle - x
        else:
            x = math.fabs(self.angle - self.new_angle) / 2
            if x < 1:
                self.angle = self.new_angle
            else:
                self.angle = self.angle + x

        theta = self.angle * math.pi / 180
        delta_x = self.speed * math.cos(theta)
        delta_y = self.speed * math.sin(theta)
        new_position = (int(self.position[0] + delta_x), int(self.position[1] + delta_y))

        if new_position[1] < 0 or new_position[1] >= self.board_size:
            self.angle = round(360 - self.angle, 2)
            self.new_angle = self.angle
            return

        if new_position[0] < 0 or new_position[0] >= self.board_size:
            self.angle = round(self.angle + 90, 2)
            self.new_angle = self.angle
            return


        self.position = new_position