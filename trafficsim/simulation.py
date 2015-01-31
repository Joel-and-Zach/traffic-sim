from trafficsim.car import Car
import random
import numpy as np


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
        last_car = self.traffic[-1]
        first_car = self.traffic[0]
        if last_car.back >= self.road - 24:
            self.end_of_line(last_car, first_car)
        if last_car.check_buffer(first_car):
            last_car.set_speed(first_car.speed)
        else:
            self.speed_or_slow(last_car)
        for car in self.traffic[-2::-1]:
            location = self.traffic.index(car)
            next_car = self.traffic[location + 1]
            if car.back >= self.road - 24:
                self.end_of_line(car, next_car)
            if car.check_buffer(next_car):
                car.set_speed(next_car.speed)
            else:
                self.speed_or_slow(car)

    def end_of_line(self, car, next_car):
        if (car.back + 24) % self.road >= next_car.back:
            car.set_speed(next_car.speed)


    def speed_or_slow(self, car):
        if random.random() > car.slow_chance:
            car.speed_up()
            if car.speed > car.max_speed:
                car.speed = car.max_speed
        else:
            if car.speed - 2 < 0:
                car.set_speed(0)
            else:
                car.slow_down()

    def over_1000(self, car, next_car):
        if (car.back + car.speed) % self.road >= next_car.back:
            distance = (next_car.back - (car.size + 1))
            if distance < 0:
                car.set_position(self.road + distance)
            else:
                car.set_position(distance)
        else:
            car.move(self.road)


    def move_logic(self, car, next_car):
        if car.back > next_car.back:
            if car.back + car.speed > self.road:
                self.over_1000(car, next_car)
            else:
                car.move(self.road)
        else:
            if self.hit(car, next_car):
                distance = (next_car.back - (car.size + 1))
                car.set_position(distance)
            else:
                car.move(self.road)


    def move_cars(self):
        last_car = self.traffic[-1]
        first_car = self.traffic[0]
        self.move_logic(last_car, first_car)
        for car in self.traffic[-2::-1]:
            location = self.traffic.index(car)
            next_car = self.traffic[location + 1]
            self.move_logic(car, next_car)
            # if last_car.back > first_car.back:
            # if car.back + car.speed > self.road:
            #     self.over_1000(car, next_car)
            # elif self.hit(car, next_car):
            #     distance = next_car.back - (car.size + 1)
            #     car.set_position(distance)
            # else:
            #     car.move(self.road)


    def hit(self, car, next_car):
        return (car.back + car.speed >= next_car.back and next_car.back - car.back > 0)


    def create_cars(self, number_of_cars):
        cars = []
        for number in range(number_of_cars):
            cars.append(Car((number_of_cars * number)))
        return cars
