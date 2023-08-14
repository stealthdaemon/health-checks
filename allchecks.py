#!/usr/bin/env python3

import os
import sys
import shutil
import psutil


def check_reboot():
    """Return True if reboot is scheduled, False if none"""
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_absolute, min_percent):
    """Returns True if there isn't enough disk space"""
    disk_usage = shutil.disk_usage(disk)
    # calculate free disk percent
    percent_free = (100 * disk_usage.free) / disk_usage.total
    # convert free disk space to
    gigabyte_free = disk_usage.free / 2**30  # 1 billion bytes make up a gb, binary notation is 2**30
    if gigabyte_free < min_absolute or percent_free < min_percent:
        return True
    return False


def check_no_network():
    pass


def check_cpu_constrained():
    """returns True if cpu usage < 75, false if it isn't"""
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage < 75


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    if check_disk_full("/", 2, 10):
        print("Disk full")
        sys.exit(1)

    print("Everything OK!")
    sys.exit(0)


if __name__ == "__main__":
    main()
