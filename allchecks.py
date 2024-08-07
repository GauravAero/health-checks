#!/usr/bin/env python
import shutil
import sys
import os

def check_reboot():
    return os.path.exists('/run/reboot-required')

def check_disk_full(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False
def check_root_full():
    '''Returns True if the root partition is full, False otherwise.'''
    return check_disk_full(disk='/',min_gb=2,min_percent=10)


def main():
    checks=[
        (check_reboot,'Pending Reboot'),
        (check_root_full,'Root partition full')
    ]
    everything_ok=True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok=False

    if not everything_ok:
        sys.exit(1)

    print('Everything OK.')
    sys.exit(0)

main()
