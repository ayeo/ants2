import numpy as np

from core.Ant import Ant

class World():
    ants = []
    nest = (0, 0)
    food = (0, 0, 0, 0)
    counter = 0
    frequency = 1000

    def __init__(self, size):
        self.size = size
        self.pheromones = np.full((size, size), 0.0, dtype=float)

    def breed_ant(self):
        id = len(self.ants)
        ant = Ant(id, (self.nest[0], self.nest[1]), self.size)
        self.ants.append(ant)


    def update(self):
        if self.counter == self.frequency:
            if (len(self.ants) < self.number):
                self.counter = 0
                self.breed_ant()

        for ant in self.ants:
            ant.update(self.pheromones)
            ant.leave_pheromone(1)
            self.leave_pheromone(ant.position, 1)

            if ant.carrying == False and \
                    ant.position[0] > self.food[0] and ant.position[0] < self.food[0] + self.food[2] and \
                    ant.position[1] > self.food[1] and ant.position[1] < self.food[1] + self.food[3]:
                ant.breadcrumb = []
                ant.breadcrumb.append(ant.position)
                ant.pheromones = np.full((self.size, self.size), 0.0, dtype=float)
                ant.carrying = True

            if ant.carrying == True and \
                    ant.position[0] > self.nest[0] and ant.position[0] < self.nest[0] + self.nest[2] and \
                    ant.position[1] > self.nest[1] and ant.position[1] < self.nest[1] + self.nest[3]:
                ant.breadcrumb = []
                ant.breadcrumb.append(ant.position)
                ant.pheromones = np.full((self.size, self.size), 0.0, dtype=float)
                ant.carrying = False

        self.counter = self.counter + 1


    def evaporate(self, quantity):
        self.pheromones = self.pheromones - quantity
        self.pheromones = np.round(self.pheromones, 5)
        self.pheromones = np.array([[max(0.00, x) for x in y] for y in self.pheromones])

    def leave_pheromone(self, position, quantity):
        self.pheromones[position] = self.pheromones[position] + quantity

    def ants_number(self, number, frequency):
        self.number = number
        self.frequency = frequency