#!/usr/bin/env python3
import sys
import time
from probe_hdrs import *

def main():
    probe_pkt = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=2) / \
                ProbeFwd(egress_spec=2) / \
                ProbeFwd(egress_spec=1)
    while True:
        try:
            sendp(probe_pkt, iface='eth0')
            # time.sleep(0.1)#0.1
            time.sleep(0.5)#0.1
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()
