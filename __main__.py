import datetime
import time
import requests
import argparse
import prometheus

PROMETHEUS = ''
parser = argparse.ArgumentParser(description='Script check server metrics. Usage : python3 __main__.py <server> ')
parser.add_argument('instance')
parser.add_argument('timeline')

if __name__ == "__main__":
  args = parser.parse_args()
  instance = args.instance
  timeline = args.timeline
  Memory_Usage()
