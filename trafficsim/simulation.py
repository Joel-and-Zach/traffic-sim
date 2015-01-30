from trafficsim.car import Car
import random


class Simulation:
    """
    Responsibilites:
    Increments time by seconds
    Moves cars, and decides
    """
    def __init__(self, time=500, number_of_cars=30, length=1000):
        self.time = 0
        self.traffic = self.create_cars(number_of_cars)
        self.road = length

    #def simulation(self):
    #    while length > time:


    def adjust_speeds(self):
        if self.traffic[-1].back +24 % self.road >= self.traffic[0].back:
            self.traffic[-1].set_speed(self.traffic[0].speed)
        for car in self.traffic[-2::-1]:
            location = self.traffic.index(car)
            car.check_buffer(self.traffic[location + 1])
            if random.random() > car.slow_chance:
                car.speed_up()
                if car.speed > car.max_speed:
                    car.speed = car.max_speed
            else:
                if car.speed - 2 < 0:
                    car.set_speed(0)
                else:
                    car.slow_down()



    #def move_cars(self):
    #    for car in self.traffic:




    def create_cars(self, number_of_cars):
        cars = []
        for number in range(number_of_cars):
            cars.append(Car((number_of_cars * number)))
        return cars
