import pyrtl

def fib(n,reset,first,second):
    a = pyrtl.Register(bitwidth=32, name='a')
    b = pyrtl.Register(bitwidth=32, name='b')
    i = pyrtl.Register(bitwidth=32, name='i')
    local_n = pyrtl.Register(bitwidth=32, name='local_n')
    done = pyrtl.WireVector(bitwidth=1, name='done')

    with pyrtl.conditional_assignment:
        with reset:
            local_n.next |= n
            i.next |= 0
            a.next |= first
            b.next |= second
        with pyrtl.otherwise:
            i.next |= i + 1
            a.next |= b
            b.next |= a + b
    done <<= i == local_n
    return a

A = pyrtl.Input(bitwidth=32,name='A')
B = pyrtl.Input(bitwidth=32,name='B')
reset = pyrtl.Input(bitwidth=1,name='reset')
n = pyrtl.Input(bitwidth=32,name='n')
result = pyrtl.Output(bitwidth=32,name='result')
result<<=fib(n,reset,A,B)

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(16):
    if cycle==0:
        sim.step({
                'n' : 16,
                'A' : 3,
                'B' : 3,
                'reset' : 1
                })
    else:
        sim.step({
                'n' : 16,
                'A' : 0,
                'B' : 0,
                'reset' : 0
                })

sim_trace.render_trace()

