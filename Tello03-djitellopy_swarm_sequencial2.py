from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.0.101",
    "192.168.0.102",
    "192.168.0.103",
    "192.168.0.104"
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
swarm.move_up(50)

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_up(i * 20 + 20))

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_left(i * 20 + 20))

swarm.land()
swarm.end()