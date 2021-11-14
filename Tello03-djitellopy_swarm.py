from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.0.101",
    "192.168.0.102"
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
swarm.move_up(50)

# run in parallel on all tellos
swarm.move_forward(50)

# run in parallel on all tellos
swarm.rotate_clockwise(180)

# run in parallel on all tellos
swarm.move_forward(50)

# run in parallel on all tellos
swarm.rotate_counter_clockwise(180)

# run in parallel on all tellos
swarm.move_left(50)

# run in parallel on all tellos
swarm.move_right(50)

swarm.land()
swarm.end()