import numpy as np

from core.Ant import Ant

class World():
    ants = []
    nest = (0, 0)
    counter = 0
    frequency = 1000

    def __init__(self, size):
        self.size = size
        self.pheromones = np.full((size, size), 0.0, dtype=float)

    def breed_ant(self):
        id = len(self.ants)
        ant = Ant(id, self.nest, self.size)
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