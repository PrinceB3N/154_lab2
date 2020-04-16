import pyrtl

def fib(first,second):
    a = pyrtl.Register(bitwidth=32, name='a')
    b = pyrtl.Register(bitwidth=32, name='b')
    with pyrtl.conditional_assignment:
        with a==0:
            with b==0:
                a.next|=first
                b.next|=second
        with pyrtl.otherwise:
            a.next |= b
            b.next |= a + b
    return b

A = pyrtl.Input(bitwidth=32,name='A')
B = pyrtl.Input(bitwidth=32,name='B')
result = pyrtl.Output(bitwidth=32,name='result')
result<<=fib(A,B)

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(16):
        sim.step({
                'A' : 3,
                'B' : 3
            })

sim_trace.render_trace()

