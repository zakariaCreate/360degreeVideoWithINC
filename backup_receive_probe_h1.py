#!/usr/bin/env python3

from probe_hdrs import *
import time
# start_time = time.time_ns()


def expand(x):
    yield x
    while x.payload:
        x = x.payload
        yield x

firstData = 1

def handle_pkt(pkt):
    global firstData
    if ProbeData in pkt:
        data_layers = [l for l in expand(pkt) if l.name=='ProbeData']

        for sw in data_layers:
            utilization = 0 if sw.cur_time == sw.last_time else 8.0*sw.byte_cnt/(sw.cur_time - sw.last_time)
            # passtime = (sw.last_time/1000000)
            # print(("Switch {} - Port {}: {} Mbps  : Time {}".format(sw.swid, sw.port, utilization, passtime)))
            # print(("S{},P{};{};{};".format(sw.swid, sw.port, utilization, time.time_ns()-start_time)), end="")
            #if sw.swid == 2 and sw.port == 4 :
                #print(("{};".format(time.time_ns())), end="")
            #print(("{};".format(utilization)), end="")
            if firstData :
                print("S{},P{};".format(sw.swid, sw.port), end="")
            else :
                if sw.swid == 1 and sw.port == 1 :
                    print(("{};".format(time.time_ns())), end="")
                print(("{};".format(utilization)), end="")
        print("")
        firstData = 0


def main():
    iface = 'eth0'
    # print(("sniffing on {}".format(iface)))
    # print("switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;")
    print("Time;", end="")
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))


if __name__ == '__main__':
    main()
