from trafficsim.car import Aggressive
from trafficsim.car import Car
from trafficsim.car import Commercial
import random
import numpy as np


class Simulation:

    """
    Responsibilites:
    Increments time by seconds
    Moves cars, and decides
    """

    def __init__(self, number_of_cars=30, length=1000, nightmare=False):
        if nightmare is False:
            self.traffic = self.create_cars(number_of_cars)
        else:
            self.traffic = self.create_nightmare(number_of_cars)
        self.road = length

    def simulate_for_speeds(self, desired_time=300):
        time = 0
        cars_speeds = []
        while desired_time > time:
            self.adjust_speeds()
            self.move_cars()
            if time > 59:
                cars_speeds.extend([car.speed for car in self.traffic])
            time += 1
        return cars_speeds


    def simulate_for_positions(self, desired_time=300):
        time = 0
        cars_positions = []
        while desired_time > time:
            self.adjust_speeds()
            self.move_cars()
            if time > 59:
                cars_positions.append([car.back for car in self.traffic])
            time += 1
        return cars_positions

    def speed_logic(self, car, next_car):
        if car.back >= self.road - 24:
            self.end_of_line(car, next_car)
        if car.check_buffer(next_car):
            if next_car.speed < car.speed:
                car.set_speed(next_car.speed)
            else:
                self.speed_or_slow(car)
        else:
            self.speed_or_slow(car)

    def adjust_speeds(self):
        last_car = self.traffic[-1]
        first_car = self.traffic[0]
        self.speed_logic(last_car, first_car)
        for car in self.traffic[-2::-1]:
            location = self.traffic.index(car)
            next_car = self.traffic[location + 1]
            self.speed_logic(car, next_car)

    def end_of_line(self, car, next_car):
        if (car.back + 24) % self.road >= next_car.back:
            if car.speed > next_car.speed:
                car.set_speed(next_car.speed)
            else:
                self.speed_or_slow(car)

    def change_slow_chance(self, car):
        if car.back < 1000:
            return 1
        elif car.back < 2000:
            return 1.4
        elif car.back < 3000:
            return 1
        elif car.back < 4000:
            return 2
        elif car.back < 5000:
            return 1
        elif car.back < 6000:
            return 1.2
        else:
            return 1

    def speed_or_slow(self, car):
        modifier = self.change_slow_chance(car)
        if random.random() > car.slow_chance * modifier:
            car.speed_up()
            if car.speed > car.max_speed:
                car.set_speed(car.max_speed)
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
            car.set_speed(0)
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
                car.set_speed(0)
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

    def hit(self, car, next_car):
        return (car.back + car.speed >= next_car.back and
                next_car.back - car.back > 0)

    def create_nightmare(self, number_of_cars):
        cars = []
        for number in range(number_of_cars):
            random_number = random.random()
            if random_number > 0.90:
                cars.append(Commercial((33 * len(cars))))
            elif random_number > 0.75:
                cars.append(Aggressive((33 * len(cars))))
            else:
                cars.append(Car((33 * len(cars))))
        return cars

    def create_cars(self, number_of_cars):
        cars = []
        for number in range(number_of_cars):
            cars.append(Car((33 * number)))
        return cars
