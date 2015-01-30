from trafficsim.car import Car
from trafficsim.road import Road


best_car = Car(5)
best_car.speed_up()
best_car.speed_up()
little_road = Road()


def test_car_speed_up():
    assert best_car.current_speed == 4
    best_car.speed_up()
    assert best_car.current_speed == 6
    best_car.speed_up()
    assert best_car.current_speed == 8

def test_car_slow_down():
    best_car.slow_down()
    assert best_car.current_speed == 6
    best_car.slow_down()
    assert best_car.current_speed == 4

def test_car_position():
    assert best_car.back == 5


def test_car_movement():
    best_car.move()
    assert best_car.back == 9

def test_car_match_speed():
    little_road.traffic[0].match_speed(best_car)
    assert little_road.traffic[0].current_speed == 4
    little_road.traffic[1].match_speed(little_road.traffic[0])
    assert little_road.traffic[1].current_speed == 4
