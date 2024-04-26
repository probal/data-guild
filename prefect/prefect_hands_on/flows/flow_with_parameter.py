from prefect import flow, task, get_run_logger


@task(retries=2, retry_delay_seconds=5)
def do_sum(a, b):
    logger = get_run_logger()
    sum_value = a + b
    logger.info(f"Sum of {a} and {b} is {sum_value}")
    return sum_value


@flow
def flow_with_parameter(a: int, b: int):
    do_sum(a, b)


if __name__ == "__main__":
    flow_with_parameter(a=2, b=4)
