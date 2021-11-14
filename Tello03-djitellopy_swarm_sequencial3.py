from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.0.101",
    "192.168.0.102",
    "192.168.0.103"

])

swarm.connect()
swarm.takeoff()

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_up(i * 50 + 20))

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_forward(i * 50 + 20))

# run in parallel on all tellos
swarm.move_left(50)

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_back(i * 50 + 20))

swarm.land()
swarm.end()