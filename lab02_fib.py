import pyrtl

def fib(n,first,second):
    a = pyrtl.Register(bitwidth=32, name='a')
    b = pyrtl.Register(bitwidth=32, name='b')

    with pyrtl.conditional_assignment:
        with n==0:
            a.next |= first
            b.next |= second
        with pyrtl.otherwise:
            a.next |= b
            b.next |= a + b
    return b

A = pyrtl.Input(bitwidth=32,name='A')
B = pyrtl.Input(bitwidth=32,name='B')
n = pyrtl.Input(bitwidth=32,name='n')
result = pyrtl.Output(bitwidth=32,name='result')
result<<=fib(n,A,B)

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(16):
    if cycle==0:
        sim.step({
                'n' : cycle,
                'A' : 3,
                'B' : 3,
                })
    else:
        sim.step({
                'n' : cycle,
                'A' : 3,
                'B' : 3,
                })

sim_trace.render_trace()

