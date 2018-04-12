
# Command is a 16 bit unsigned integer on the crazyflie 
# So value must be between 0 and 65536
def thrust(command_arg):
	return 2.130295e-11 * command_arg * command_arg + 1.032633e-6 * command_arg + 5.48456e-4

def angularVelocity(command_arg):
	return 0.04076521 * command_arg + 380.8359

def torque(thrust_arg):
	return 0.005964552* thrust_arg + 1.563383e-5;

#############################################"#################################"
# Calculate  the motor constant parameter
motor_constant_moy = 0
nb_command = 2**16

for i in range(nb_command):
	ang_vel = angularVelocity(i)
	curr_motor_constant = thrust(i) / (ang_vel * ang_vel)
	motor_constant_moy = motor_constant_moy + curr_motor_constant
motor_constant_moy = motor_constant_moy / nb_command

print motor_constant_moy

###############################################################################
# Calculate the moment constant for simulation
moment_constant_moy = 0

for i in range(nb_command):
	thrust_i = thrust(i)
	torque_i = torque(thrust_i)
	moment_constant_moy = moment_constant_moy + (torque_i/thrust_i)
moment_constant_moy = moment_constant_moy / nb_command

print moment_constant_moy

###############################################################################
# max rotor velocity

print angularVelocity(2**16 - 1)
