from trafficsim.car import Car


best_car = Car()
best_car.speed_up()
best_car.speed_up()


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

def test_car_stop():
    best_car.stop()
    assert best_car.current_speed == 0
