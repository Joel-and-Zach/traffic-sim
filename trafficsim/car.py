import random

class Car:

    def __init__(self):
        self.max_speed = 33.33
        self.current_speed = 0
        self.size = 5
        self.acceleration = 2
        self.space = 20

    def speed_up(self):
        self.current_speed += self.acceleration

    def slow_down(self):
        self.current_speed -= self.acceleration

    def stop(self):
        self.current_speed = 0
