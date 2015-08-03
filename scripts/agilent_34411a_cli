#!/usr/bin/env python

import argparse
import time
import sys
import logging

from agilent_34411A import Agilent_34411A

try:
    clock = time.perf_counter
except:
    clock = time.time

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

def T(R):
    return -5.67E-6 * R**3 + 0.0024984 * R**2 + 2.22764 * R - 242.078

def R(U,I):
    return U/I

def T_U(U):
    return T(R(U,400E-6))

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('host', help='Agilent 34411A to connect to')
    parser.add_argument('--port', type=int, default=5025, help='TCP Port to connect to')
    parser.add_argument('--interval', type=float, default=0.3, help='Interval in s between printing the value')
    parser.add_argument('--avg-samples', type=int, default=1, help='Number of samples to to capture for averaging')
    parser.add_argument('--value-scaling', type=float, default=1.0, help='A factor to scale the measured value with')
    parser.add_argument('--output-format', default="{:.03f}", help='Format for printing the output')
    parser.add_argument('--apply-function', choices=('None', 'PT100'), help='A function to apply to the output value (after scaling)')
    args = parser.parse_args()

    a = Agilent_34411A(args.host, args.port)
    print("\nConnected to the following device:\n" + a.idn + "\n")

    sampling_interval = args.interval/args.avg_samples
    last_time = clock() - 0.5 * sampling_interval
    values = []
    i = 1
    while True:
        if last_time + sampling_interval < clock():
            logger.warning("The sampling time doesn't currently allow you at to measure at the desired frequency.")
        while clock() - last_time < sampling_interval:
            time.sleep(0.005)
        i += 1
        last_time += sampling_interval
        value = a.read()
        value *= args.value_scaling
        if args.apply_function == 'PT100':
            value = T_U(value)
        values.append(value)
        if i%args.avg_samples == 0:
            print(args.output_format.format(sum(values)/len(values)))
            values = []

if __name__ == "__main__":
    main()

