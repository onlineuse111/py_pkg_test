#!/usr/bin/env python2.7

import time

def main():
    c = ' SHRAVYA  '
    intr = 0.6
    while True:
        for i in xrange(1, 50, 2):
            print c*i
            time.sleep(intr)
        for i in xrange(50, 1, -2):
            print c*i
            time.sleep(intr)
        
if __name__ == '__main__':
    main()
