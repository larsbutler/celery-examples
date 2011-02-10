import tasks

def make_pi_tasks():
    num_calcs = [10**5, 10**6, 10**7]
    pending_tasks = []

    # dispatch the tasks to available workers
    print "Dispatching tasks"
    for x in num_calcs:
        pending_tasks.append(tasks.make_pi.delay(x))

    results = []
    # now wait for the tasks to complete,
    # then gather results
    for task in pending_tasks:
        task.wait()
        if not task.status == 'SUCCESS':
            raise Exception(task.result)
        results.append(task.result)

    print "Results:"
    for i in results:
        print i


if __name__ == '__main__':
    print "Making pi..."
    make_pi_tasks()
