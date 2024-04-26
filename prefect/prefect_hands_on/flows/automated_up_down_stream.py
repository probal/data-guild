from prefect import flow, task


@flow(log_prints=True)
def automated_up_down_stream():
    upstream_result = upstream.submit()
    downstream_1_result = downstream_1.submit(upstream_result)
    downstream_2_result = downstream_2.submit(upstream_result)
    mapped_task_results = mapped_task.map([downstream_1_result, downstream_2_result])
    final_task(mapped_task_results)


@task
def upstream():
    return "Hello from upstream!"


@task
def downstream_1(input_data):
    return input_data


@task
def downstream_2(input_data):
    return input_data


@task
def mapped_task(input_data):
    return input_data


@task
def final_task(input_data):
    print(input_data)


if __name__ == "__main__":
    automated_up_down_stream()
