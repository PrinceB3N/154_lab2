### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
# < add your code here >
a = pyrtl.Input(bitwidth=3, name='a')
b = pyrtl.Input(bitwidth=3, name='b')
c = pyrtl.Input(bitwidth=3,name='c')
d = pyrtl.Input(bitwidth=3,name='d')
e = pyrtl.Input(bitwidth=3,name='e')
# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
# < add your code here >
output = pyrtl.Output(bitwidth=3,name='output')
# Describe your 5:1 MUX implementation
# < add your code here >
with pyrtl.conditional_assignment:
    with s == 0b000:
        output |= a
    with s == 0b001:
        output |= b
    with s == 0b010:
        output |= c
    with s == 0b011:
        output |= d
    with s == 0b100:
        output |= e
# Simulate and test your design for 16 cycles using random inputs
# < add your code here >
import random

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
arr = [0,1,2,3,4,5,6,7]
choice = [0,1,2,3,4]
for cycle in range(16):
      # Call "sim.step" to simulate each clock cycle of the design
    sim.step({
          'a': random.choice(arr),
          'b': random.choice(arr),
          'c': random.choice(arr),
          'd': random.choice(arr),
          'e': random.choice(arr),
          's': random.choice(choice)
             })
# Print the trace results to the screen.
print('--- 3-bit 5:1 MUX Simulation')
sim_trace.render_trace()
    
