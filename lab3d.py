#!/usr/bin/env python3
'''Lab 3 Inv 3 - Free Disk Space Check'''
# Author ID: akharel2

import os
import subprocess

def free_space():
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def run_os_system():
    print("Running os.system commands:")
    os.system('ls')
    os.system('whoami')
    os.system('ifconfig')

def run_os_popen():
    print("\nRunning os.popen commands:")
    print('The contents of ls_return:', os.popen('ls').read().strip())
    print('The contents of whoami_return:', os.popen('whoami').read().strip())
    print('The contents of ifconfig_return:', os.popen('ifconfig').read().strip())

def run_subprocess_popen():
    print("\nRunning subprocess.Popen commands:")
    p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    print(stdout)

if __name__ == '__main__':
    print(free_space())
    run_os_system()
    run_os_popen()
    run_subprocess_popen()
