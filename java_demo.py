import tasks

if __name__ == "__main__":
    print "Dispatching task"
    task = tasks.java_task.delay(42)
    print "Waiting for task to complete"
    task.wait()
    print "Task is complete"
    print "task.state is %s" % task.state 
    print "task.result is %s" % task.result
    print "Done"
