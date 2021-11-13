# Import the necessary modules
import socket
import threading
import time

# Name the IP and Port of Tello
tello1_address = ('192.168.0.101', 8889)
tello2_address = ('192.168.0.102', 8889)
tello3_address = ('192.168.0.103', 8889)
tello4_address = ('192.168.0.104', 8889)

# IP and Port of local computer
local1_address = ('', 9010)
local2_address = ('', 9011)
local3_address = ('', 9012)
local4_address = ('', 9013)

# Create a UDP connection that we'll send the command to
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock1.bind(local1_address)
sock2.bind(local2_address)
sock3.bind(local3_address)
sock4.bind(local4_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock1.sendto(message.encode(), tello1_address)
    sock2.sendto(message.encode(), tello2_address)
    sock3.sendto(message.encode(), tello3_address)
    sock4.sendto(message.encode(), tello4_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response1, ip_address = sock1.recvfrom(128)
      response2, ip_address = sock2.recvfrom(128)
      response3, ip_address = sock3.recvfrom(128)
      response4, ip_address = sock4.recvfrom(128)
      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #3: " + response3.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #4: " + response4.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock1.close()
      sock2.close()
      sock3.close()
      sock4.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Each leg of the box will be 100 cm. Tello uses cm units by default.
flight_distance = 50

# Yaw 90 degrees
yaw_angle = 360

# Put Tello into command mode
send("command", 3)

# Send the takeoff command
send("takeoff", 8)

# Loop maneuver 3 times
for i in range(3):
  # Fly right
    send("right " + str(flight_distance), 5)
    
  # Fly left
    send("left " + str(flight_distance), 5)
    
  # Yaw right
    send("cw " + str(yaw_angle), 10)

# Land
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()
sock2.close()
sock3.close()
sock4.close()