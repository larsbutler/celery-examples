from celery.decorators import task

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

@task
def make_pi_task(num_calcs):
    """
    Task which calls the make_pi function to approximate pi.

    This is just a simple example of how can create tasks using plain functions.
    """
    return make_pi(num_calcs)


class TaskTest(object):
    """
    Simple skeleton class to demonstrate how celery tasks work on objects.
    """

    def __init__(self, pi_calcs):
        """
        :param pi_calcs: Number of iterations we want to use to approximate pi.
        :type pi_calcs: integer
        """
        self.pi_calcs = pi_calcs
        assert isinstance(self.pi_calcs, int)

    @task
    def make_pi(self):
        """
        Task which calls the make_pi function to approximate pi.

        This is just a simple example of how one can create tasks using object
        instance methods.
        """
        return make_pi(self.pi_calcs)
