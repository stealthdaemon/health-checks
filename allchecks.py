#!/usr/bin/env python3

import os


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
    pass

if __name__ == "__main__":
    main()
