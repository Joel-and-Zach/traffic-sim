from trafficsim.car import Car
from trafficsim.road import Road
import random


class Simulation:
    """
    Responsibilites:
    Increments time by seconds
    Moves cars, and decides
    """
    def __init__(self, time=500, number_of_cars=30, length=1000):
        self.time = 0
        self.traffic = create_cars()
        self.road = length

    def simulation(self):
        while length > time:


    def adjust_speed(self, road):
        for car in self.road.traffic[::-1]:
            if  random.random() > self.car.slow_chance:
                if car.current_speed + 2 > car.max_speed:
                    car.
                    pass
                car.speedup():
            else:

    def create_cars(self, number_of_cars):
        cars = []
        for number in range(number_of_cars):
            cars.append(Car((number_of_cars * number)))
        return cars
