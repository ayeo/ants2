import numpy as np

from core.Ant import Ant

class World():
    ants = []
    nest = (0, 0)
    food = (0, 0, 0)
    counter = 0
    number = 1
    frequency = 1000

    def __init__(self, size):
        self.size = size
        self.pheromones_nest = np.full((size, size), 0.0, dtype=float)
        self.pheromones_food = np.full((size, size), 0.0, dtype=float)

    def breed_ant(self):
        id = len(self.ants)
        ant = Ant(id, (self.nest[0], self.nest[1]), self.size)
        self.ants.append(ant)

    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.frequency:
            if (len(self.ants) < self.number):
                self.counter = 0
                self.breed_ant()

        for ant in self.ants:
            if ant.carrying:
                ant.update(ant.memory)
            else:
                ant.update(self.pheromones_food)

            ant.leave_pheromone(1)
            self.leave_pheromone(ant.position, 1, ant.carrying)


            ant.step = ant.step + 1
            if (ant.step > 100):
                ant.position = (self.nest[0], self.nest[1])
                ant.reset()
                return


            if self.is_on_food(ant) and ant.carrying == False:
                ant.reset()
                ant.carrying = True
                ant.leave_pheromone(1)
                self.leave_pheromone(ant.position, 1, ant.carrying)

            elif self.is_on_nest(ant) and ant.carrying:
                ant.reset()
                ant.carrying = False
                ant.position = (self.nest[0], self.nest[1])
                ant.leave_pheromone(1)
                self.leave_pheromone(ant.position, 1, ant.carrying)


    def is_on_food(self, ant: Ant):
        return \
            ant.position[0] > self.food[0] - self.food[2] and ant.position[0] < self.food[0] + self.food[2] and \
            ant.position[1] > self.food[1] - self.food[2] and ant.position[1] < self.food[1] + self.food[2]


    def is_on_nest(self, ant: Ant):
        return \
            ant.position[0] > self.nest[0] - self.nest[2] and ant.position[0] < self.nest[0] + self.nest[2] and \
            ant.position[1] > self.nest[1] - self.nest[2] and ant.position[1] < self.nest[1] + self.nest[2]

    def evaporate(self, quantity):
        self.pheromones_nest = self.pheromones_nest - quantity
        self.pheromones_nest = np.round(self.pheromones_nest, 5)
        self.pheromones_nest = np.array([[max(0.00, x) for x in y] for y in self.pheromones_nest])
        self.pheromones_nest = np.array([[min(5.00, x) for x in y] for y in self.pheromones_nest])

        self.pheromones_food = self.pheromones_food - quantity
        self.pheromones_food = np.round(self.pheromones_food, 5)
        self.pheromones_food = np.array([[max(0.00, x) for x in y] for y in self.pheromones_food])
        self.pheromones_food = np.array([[min(5.00, x) for x in y] for y in self.pheromones_food])


    def leave_pheromone(self, position, quantity, carrying):
        if carrying:
            self.pheromones_food[position] = self.pheromones_food[position] + quantity
        else:
            self.pheromones_nest[position] = self.pheromones_nest[position] + quantity


    def ants_number(self, number, frequency):
        self.number = number
        self.frequency = frequency