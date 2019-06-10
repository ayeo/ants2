import numpy as np

from core.Ant import Ant

class World():
    ants = []
    nest = (0, 0)

    def __init__(self, size):
        self.size = size
        self.pheromones = np.full((size, size), 0.01, dtype=float)

    def breed_ant(self):
        id = len(self.ants)
        ant = Ant(id, self.nest, self.size)
        self.ants.append(ant)

    def update(self):
        for ant in self.ants:
            ant.update()
            self.leave_pheromone(ant.position, 1)

    def leave_pheromone(self, position, quantity):
        self.pheromones[position] = self.pheromones[position] + quantity
