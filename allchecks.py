#!/usr/bin/env python3

import os
import sys
import shutil
import psutil
import socket


def check_reboot():
    """Return True if reboot is scheduled, False if none"""
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space"""
    disk_usage = shutil.disk_usage(disk)
    # calculate free disk percent
    percent_free = (100 * disk_usage.free) / disk_usage.total
    # convert free disk space to
    gigabyte_free = disk_usage.free / 2**30  # 1 billion bytes make up a gb, binary notation is 2**30
    if gigabyte_free < min_gb or percent_free < min_percent:
        return True
    return False


def check_full_root():
    return check_disk_full(disk="/", min_absolute=2, min_percent=10)


def check_no_network():
    """Check network status"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except socket.gaierror:
        return True


def check_cpu_constrained():
    """returns True if cpu usage < 75, false if it isn't"""
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage < 75:
        return False
    return True


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    if check_full_root():
        print("Disk full")
        sys.exit(1)

    if check_cpu_constrained():
        print("CPU usage high")
        sys.exit(1)

    if check_no_network():
        print("No network")
        sys.exit(1)

    print("Everything OK!")
    sys.exit(0)


if __name__ == "__main__":
    main()
