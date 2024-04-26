from prefect import flow, task


@flow(log_prints=True)  # Default task runner is ConcurrentTaskRunner
def dependencies_example():
    # no dependencies, execution is order not guaranteed
    first.submit()
    second.submit()
    third.submit()

    print("==============")
    with_dependency()


@flow(log_prints=True)
def with_dependency():
    first_result = first.submit()
    second_result = second.submit(first_result)
    third.submit(second_result)


@task
def first():
    print("I'm first!")


@task
def second(input_data=None):
    print("I'm second!")


@task
def third(input_data=None):
    print("I'm third!")
