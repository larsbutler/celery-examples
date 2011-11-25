from celery.task.sets import TaskSet

import tasks

NUM_CALCS = [10**5, 10**6, 10**7]

def make_pi_tasks():

    taskset = TaskSet(tasks.make_pi.subtask((x, )) for x in NUM_CALCS)
    print "Dispatching tasks"
    taskset_result = taskset.apply_async()

    print "Waiting for results"
    results = taskset_result.join_native()
    print "Results:"
    for i in results:
        print i


if __name__ == '__main__':
    print "Making pi"
    make_pi_tasks()
