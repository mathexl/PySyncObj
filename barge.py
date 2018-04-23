#!/usr/bin/env python
import sys
import time
from pprint import pprint
from pysyncobj import SyncObj, replicated
import test_syncobj as test_syncobj


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[1])
    partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]
    test_syncobj.test_autoTick()
    #test_syncobj.test_syncThreeObjectsLeaderFail()
    #o = TestObj('localhost:%d' % port, partners)
