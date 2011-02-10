from celery.decorators import task

@task
def make_pi(num_calcs):
    print "Calculating pi with %s calculations" % num_calcs
    pi = 0.0
    for k in xrange(num_calcs):
        pi += 4 * ((-1)**k / ((2.0 * k) + 1))
    return pi
