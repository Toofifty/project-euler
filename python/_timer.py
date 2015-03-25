import time, os, sys

start = time.time()
print '\n'
[os.system(arg) for arg in sys.argv[1:]]
print '\n%dms' % (1000 * (time.time() - start))