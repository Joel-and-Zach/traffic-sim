from trafficsim.simulation import Simulation


sim = Simulation()

edge_sim = Simulation(number_of_cars=2)

def test_speed():
    sim.traffic[0].speed_up()
    start_speed = sim.traffic[0].speed
    sim.adjust_speeds()
    assert start_speed != sim.traffic[0].speed

def test_edge_case():
    edge_sim.traffic[1].set_speed(30)
    edge_sim.traffic[1].set_position(990)
    edge_sim.traffic[0].set_position(10)
    edge_sim.adjust_speeds()
    assert edge_sim.traffic[1].speed == 0
