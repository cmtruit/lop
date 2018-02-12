#! /usr/bin/env python
"""
This script will be shipped to remote nodes from worker nodes in lop

"""
from __future__ import print_function
import sys
import argparse
import platform
import subprocess


def updateWithYum(os,exclude, packages):
    if exclude:
        excludes = ['--disablerepo='+'"'+s+'"' +' ' for s in exclude]
        disablerepo = ''.join(excludes)
        cmd = "yum -y update " + disablerepo
        print(cmd)
        update = subprocess.Popen(cmd, shell=True)
        update.communicate()
        print(update.returncode)
    return update.returncode


def control(os,exclude, packages):
    if os == 'centos':
       updateWithYum(os,exclude)
    if os == 'ubuntu':
       cmd = 'apt'
    if os == 'redhat':
       updateWithYum(os,exclude)
    if os == 'suse':
       cmd = 'zypper'
    return

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

def facts():
    facts = dict(
                 dist = platform.dist(),
                 linux_distribution = linux_distribution(),
                 system = platform.system(),
                 machine = platform.machine(),
                 platform = platform.platform(),
		 uname = platform.uname(),
		 version = platform.version(),
		 mac_ver = platform.mac_ver()
                 )
    return facts

def main():
    fact = facts()
    os = fact['dist'][0]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("update", action="store",help="[ update ] sets the action to update",)
    parser.add_argument( "-e","--exclude",nargs='+', help="repos to exclude, non if ommited")
    args = parser.parse_args()
    if len(sys.argv) <= 1:
        parser.print_help() 
        sys.exit(1)
    if args.update == 'update' and not args.exclude:
        control(os,exclude=None)
    elif args.update == 'update' and args.exclude:
        print(args.exclude)
        control(os,exclude=args.exclude)
    else:
        parser.print_help() 
        

if __name__ == "__main__":
    main()
