import math

def calculate_velocity_from_electric_field(electric_field, 
                                            charge, 
                                            mass,  
                                            distance_traveled):
    
    # Calculate electric force
    electric_force = charge * electric_field  

    # Calculate acceleration
    acceleration = electric_force / mass

    # Initial velocity is 0 (released from rest) 
    initial_velocity = 0  

    # Use kinematic equation for constant acceleration
    final_velocity = math.sqrt(initial_velocity**2 + 
                                2 * acceleration * distance_traveled)

    return final_velocity

# Example call
field_strength = 100  
particle_charge = 1e-6
particle_mass = 1e-6
distance = 0.1

velocity = calculate_velocity_from_electric_field(field_strength, 
                                                  particle_charge,
                                                  particle_mass,
                                                  distance)

print(f"Velocity = {velocity:.2f} m/s")
