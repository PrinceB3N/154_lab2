import pyrtl

def fib(first,second):
    a = pyrtl.Register(bitwidth=32, name='a')
    b = pyrtl.Register(bitwidth=32, name='b')
    return_val = pyrtl.WireVector(bitwidth=32,name='return_val')
    with pyrtl.conditional_assignment:
        with a==0:
            with b==0:
                a.next|=first
                b.next|=second
                return_val|=first
        with pyrtl.otherwise:
            a.next |= b
            b.next |= a + b
            return_val|=b
    
    return return_val

A = pyrtl.Input(bitwidth=32,name='A')
B = pyrtl.Input(bitwidth=32,name='B')
result = pyrtl.Output(bitwidth=32,name='result')
result<<=fib(A,B)

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(16):
        sim.step({
                'A' : 1,
                'B' : 2
            })

sim_trace.render_trace()

