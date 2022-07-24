#!/usr/bin/env python
import shutil
import sys
import os

def check_reboot():
    return os.path.exists('/run/reboot-required')

def check_disk_usage(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def main():
    if check_reboot():
        print('Pending Reboot.')
        sys.exit(1)
    if check_disk_usage(disk="/",min_gb=2,min_percent=10):
        print('Disk full.')
        sys.exit(1)

    print('Everything OK.')
    sys.exit(0)

main()
