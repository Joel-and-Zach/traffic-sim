import random

styles = ["Scion Xa", "Honda Civic", "Acura TLX", "Toyota Prius", "Honda Accord",
         "Toyota Camry"]


class Car:

    def __init__(self, position):
        self.max_speed = 33.33
        self.current_speed = 0
        self.size = 5
        self.acceleration = 2
        self.space = 20
        self.back = position
        self.type = random.choice(styles)

    def __str__(self):
        return self.style

    def __repr__(self):
        return self.__str__()

    def speed_up(self):
        self.current_speed += self.acceleration

    def slow_down(self):
        self.current_speed -= self.acceleration

    def move(self):
        self.back += self.current_speed

    def match_speed(self, other_car):
        self.current_speed = other_car.current_speed
