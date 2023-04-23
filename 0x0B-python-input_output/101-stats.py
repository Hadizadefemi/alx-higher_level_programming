#!/usr/bin/env python3

import sys
import signal

total_size = 0
status_counts = {}

def print_stats():
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def handle_interrupt(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

line_count = 0
for line in sys.stdin:
    try:
        ip, _, _, date, _, request, status, size = line.split()
        if status not in status_counts:
            status_counts[status] = 0
        status_counts[status] += 1
        total_size += int(size)
        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0
    except ValueError:
        pass

print_stats()
