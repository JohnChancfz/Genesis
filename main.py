# -*- coding: utf-8 -*-
from app import Genesis
import time

if __name__ == '__main__':
    print 'Genesis start...'
    start = time.time()
    genesis = Genesis()
    genesis.run()
    print 'Genesis end!'
    print time.time() - start
