import random

styles = ["Scion Xa", "Honda Civic", "Acura TLX", "Toyota Prius", "Honda Accord",
         "Toyota Camry"]


class Car:

    def __init__(self, position):
        self.max_speed = 33.33
        self.speed = 0
        self.size = 5
        self.acceleration = 2
        self.space = 20
        self.back = position
        self.style = random.choice(styles)
        self.slow_chance = 0.1


    def __str__(self):
        return self.style

    def __repr__(self):
        return self.__str__()

    def speed_up(self):
        self.speed += self.acceleration

    def slow_down(self):
        self.speed -= self.acceleration

    def move(self, road_length):
        self.back = (self.back + self.speed) % road_length

    def set_speed(self, speed):
        self.speed = speed

    def check_buffer(self, previous_car):
        if self.back + 24 >= previous_car.back:
            return True
        else:
            return False

    def set_position(self, position):
        self.back = position

    def set_slow_chance(self, chance):
        self.slow_chance = chance
