# If the temp of the body is changing from 100°c to 70°c in 15 min. Find when the temp will be 40°c. If the temperature of air is 30°c?

import numpy as np
def calculate_temperature(initial_temp, final_temp, room_temp, cooling_rate, time):


  # Implement Newton's Law of Cooling formula
  temperature = (initial_temp - room_temp) * np.exp(-cooling_rate * time) + room_temp

  return temperature

# Set constants
initial_temp = 100  # Initial temperature (degrees Celsius)
final_temp = 70  # Final temperature reached in the experiment (degrees Celsius)
room_temp = 30  # Room temperature (degrees Celsius)
target_temp = 40  # Target temperature to find the time for (degrees Celsius)

# Calculate the cooling rate based on the provided data
time_for_cooling = 15  # Time taken to cool from 100°C to 70°C (minutes)
cooling_rate = -np.log((final_temp - room_temp) / (initial_temp - room_temp)) / time_for_cooling

# Find the approximate time to reach the target temperature
time_to_target_temp = -np.log((target_temp - room_temp) / (initial_temp - room_temp)) / cooling_rate

print("The approximate time to reach", target_temp, "°C is", time_to_target_temp, "minutes.")
