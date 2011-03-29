import tasks

NUM_CALCS = [10**5, 10**6, 10**7]

def make_pi_tasks():
    pending_tasks = []

    print "Dispatching tasks"
    for x in NUM_CALCS:
        pending_tasks.append(tasks.make_pi_task.delay(x))

    results = get_task_results(pending_tasks)
    
    print "Results: %s" % results

def make_pi_class_tasks():
    """
    Similar to the example above, but uses some simple objects to demonstrate
    how tasks work with object instance methods.
    """
    test_objs = [tasks.TaskTest(x) for x in NUM_CALCS]

    pending_tasks = []

    print "Dispatching tasks"
    for obj in test_objs:
        pending_tasks.append(obj.make_pi.delay(obj))

    results = get_task_results(pending_tasks)

    print "Results: %s" % results
    
def get_task_results(tasks):
    """
    Wait for all tasks to complete and return a list containing the result of
    each task.
    """
    results = []

    for task in tasks:
        task.wait()
        if not task.successful():
            raise Exception(task.result)
        results.append(task.result)

    return results


if __name__ == '__main__':
    print "Making pi:"
    make_pi_tasks()

    print
    print "Making pi, with class:"
    make_pi_class_tasks()
