#!/usr/bin/env python3

from probe_hdrs import *
import time
import sys

# ***
import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')
size = 20
x_vec = np.linspace(0,size,size+1)[0:-1]
# y_vec = np.random.randn(len(x_vec))
y_vec = np.zeros(len(x_vec))
# y_vec = np.arange(0, 100, 5)
line1 = []

def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(5,2))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)
        #update plot label/title
        plt.ylabel('Network load (%)')
        # plt.xlabel('Time (x100 ms)')
        plt.xlabel('Time')
        # plt.title('BW SW1 Port1: {}'.format(identifier))
        plt.title('Network load monitoring (With INC)')
        plt.show()

    # after the figure, axis, and line are created, we only need to update the y-data
    # line1.set_ydata(y1_data)
    line1.set_data(x_vec,y1_data)
    # adjust limits if new data goes beyond bounds
    # if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        # plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])

    # plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)]) #this one is working
    plt.ylim([-1,100]) #this one is working

    # if np.min(x_vec)<=line1.axes.get_xlim()[0] or np.max(x_vec)>=line1.axes.get_xlim()[1]:
    # plt.xlim([np.min(x_vec)-np.std(x_vec),np.max(x_vec)+np.std(x_vec)])
    plt.xlim([np.min(x_vec)-1,np.max(x_vec)+1])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)

    # return line so we can update it again in the next iteration
    return line1
# ***


def expand(x):
    yield x
    while x.payload:
        x = x.payload
        yield x

firstData = 1

def handle_pkt(pkt):
    global firstData
    global size
    global x_vec
    global y_vec
    global line1
    if ProbeData in pkt:
        data_layers = [l for l in expand(pkt) if l.name=='ProbeData']
        networkLoad = 0
        for sw in data_layers:
            utilization = 0 if sw.cur_time == sw.last_time else 8.0*sw.byte_cnt/(sw.cur_time - sw.last_time)
            # passtime = (sw.last_time/1000000)
            # print(("Switch {} - Port {}: {} Mbps  : Time {}".format(sw.swid, sw.port, utilization, passtime)))
            # print(("S{},P{};{};{};".format(sw.swid, sw.port, utilization, time.time_ns()-start_time)), end="")
            #if sw.swid == 2 and sw.port == 4 :
                #print(("{};".format(time.time_ns())), end="")
            #print(("{};".format(utilization)), end="")
            if firstData :
                # print("S{},P{};".format(sw.swid, sw.port), end="")
                print("Network load (With INC);")
                firstData = 0

            if sw.swid == 3 and sw.port == 1 :
                print(("{};".format(time.time_ns())), end="")
            # print(("{};".format(utilization)), end="")
            networkLoad += utilization
            # print("Switch {} - Port {}: {} Mbps".format(sw.swid, sw.port, utilization))
            # rand_val = np.random.randn(1)
        print(("{};".format((networkLoad/1.5)*100)), end="")
        size += 1
        y_vec[-1] = (networkLoad/1.5)*100
        x_vec[-1] = size
        line1 = live_plotter(x_vec,y_vec,line1)
        y_vec = np.append(y_vec[1:],0.0)
        x_vec = np.append(x_vec[1:],0.0)
        print("")
        sys.stdout.flush()


def main():
    iface = 'eth0'
    # print(("sniffing on {}".format(iface)))
    # print("switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;switch,port;bandwidth;time;")
    print("Time;", end="")
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))


if __name__ == '__main__':
    main()
