from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the drone
vehicle = connect("udp:127.0.0.1:14550", wait_ready=True)

# Arm the drone and take off to an altitude of 1000 meters
print("Arming motors")
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.simple_takeoff(1000)

while True:
    # Wait for the drone to reach the target altitude
    print("Altitude: ", vehicle.location.global_relative_frame.alt)
    if vehicle.location.global_relative_frame.alt >= 900:
        print("Reached target altitude")
        break
    time.sleep(1)

# Go to the village of Tatev
print("Going to Tatev")
target_location = LocationGlobalRelative(39.3833863, 46.2425472, 900)
vehicle.simple_goto(target_location)

while True:
    # Wait for the drone to reach the target location
    print("Distance to target: ",
          vehicle.location.global_relative_frame.dist(target_location))
    if vehicle.location.global_relative_frame.dist(target_location) <= 10:
        print("Reached target location")
        break
    time.sleep(1)

# Take a picture
print("Taking a picture")
# Your code for taking a picture goes here

# Return to the starting point
print("Returning to launch")
vehicle.mode = VehicleMode("RTL")

while True:
    # Wait for the drone to reach the starting point
    print("Distance to launch: ",
          vehicle.location.global_relative_frame.dist(vehicle.home_location))
    if vehicle.location.global_relative_frame.dist(vehicle.home_location) <= 10:
        print("Reached launch point")
        break
    time.sleep(1)

# Land the drone
print("Landing")
vehicle.mode = VehicleMode("LAND")

# Close the connection to the drone
vehicle.close()
