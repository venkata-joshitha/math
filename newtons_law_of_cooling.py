# If the temp of the body is changing from 100°c to 70°c in 15 min. Find when the temp will be 40°c. If the temperature of air is 30°c?

import numpy as np
def calculate_temperature(initial_temp, final_temp, room_temp, cooling_rate, time):


  # Implement Newton's Law of Cooling formula
  temperature = (initial_temp - room_temp) * np.exp(-cooling_rate * time) + room_temp

  return temperature

# Set constants
initial_temp = float(input("Initial Temperature: "))
final_temp = float(input("Final Temperature: "))
room_temp = float(input("Room Temperature: "))
target_temp = float(input("Target temperature: "))

# Calculate the cooling rate based on the provided data
time_for_cooling = float(input("Time: "))
cooling_rate = -np.log((final_temp - room_temp) / (initial_temp - room_temp)) / time_for_cooling


time_to_target_temp = -np.log((target_temp - room_temp) / (initial_temp - room_temp)) / cooling_rate

print("The approximate time to reach", target_temp, "°C is", time_to_target_temp, "minutes.")
