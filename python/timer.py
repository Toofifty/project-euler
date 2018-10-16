from time import time as _time

def time(fun):
    def wrapper(*args):
        start = _time()
        ret = fun()
        print '\nanswer:', ret
        print 'in: %.4fms' % (1000 * (_time() - start))
        return ret
    return wrapper

def many(num = 100):
    def decorator(fun):
        def wrapper(*args):
            start = _time()
            min_time = 10000000
            max_time = 0
            for i in range(num):
                single_start = _time()
                ret = fun()
                taken = _time() - single_start
                if taken < min_time:
                    min_time = taken
                if taken > max_time:
                    max_time = taken
            print '#', ret
            print '# %.4fms' % (1000 * min_time)
            print '\nmin: %.4fms' % (1000 * min_time)
            print 'max: %.4fms' % (1000 * max_time)
            print 'avg: %.4fms' % (1000 * (_time() - start) / num)
            print '(repeated x%d)' % num
            return ret
        return wrapper
    return decorator