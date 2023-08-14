#!/usr/bin/env python3

import os
import sys

def check_reboot():
    """Return True if reboot is scheduled, False if none"""
    return os.path.exists("run/reboot-required")


def check_disk_full():
    pass


def check_no_network():
    pass


def check_cpu_constrained():
    pass


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    print("Everything OK!")
    sys.exit(0)

if __name__ == "__main__":
    main()
