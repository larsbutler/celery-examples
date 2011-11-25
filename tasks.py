from celery.decorators import task

@task
def make_pi(num_calcs):
    """
    Simple pi approximation based on the Leibniz formula for pi.
    http://en.wikipedia.org/wiki/Leibniz_formula_for_pi

    :param num_calcs: defines the length of the sequence
    :type num_calcs: positive int

    :returns: an approximation of pi
    """
    print "Approximating pi with %s iterations" % num_calcs
    pi = 0.0
    for k in xrange(num_calcs):
        pi += 4 * ((-1)**k / ((2.0 * k) + 1))
    return pi
