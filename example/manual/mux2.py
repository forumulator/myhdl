from __future__ import generators
from myhdl import Signal, Simulation, delay, always_comb

def mux(z, a, b, sel):
    """ Multiplexer.
    
    z -- mux output
    a, b -- data inputs
    sel -- control input: select a if asserted, otherwise b
    """
    def muxlogic():
        if sel == 1:
            z.next = a
        else:
            z.next = b

    return always_comb(muxlogic)

from random import randrange

(z, a, b, sel) = [Signal(0) for i in range(4)]

MUX_1 = mux(z, a, b, sel)

def test():
    print "z a b sel"
    for i in range(8):
        a.next, b.next, sel.next = randrange(8), randrange(8), randrange(2)
        yield delay(10)
        print "%s %s %s %s" % (z, a, b, sel)

def main():
    Simulation(MUX_1, test()).run()    
    
if __name__ == '__main__':
    main()