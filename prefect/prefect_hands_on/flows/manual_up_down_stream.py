from prefect import flow, task


@flow(log_prints=True)
def manual_up_down_stream():
    upstream_result = upstream.submit()
    downstream_1_result = downstream_1.submit(wait_for=[upstream_result])
    downstream_2_result = downstream_2.submit(wait_for=[upstream_result])
    mapped_task_results = mapped_task.map([1, 2], wait_for=[downstream_1_result, downstream_2_result])
    final_task(wait_for=mapped_task_results)


@task
def upstream():
    pass


@task
def downstream_1():
    pass


@task
def downstream_2():
    pass


@task
def mapped_task(input_data):
    pass


@task
def final_task():
    pass


if __name__ == "__main__":
    manual_up_down_stream()
