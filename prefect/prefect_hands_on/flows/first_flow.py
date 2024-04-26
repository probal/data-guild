from prefect import flow, task, get_run_logger


@task
def first_task(logger):
    logger.info("First Task")


@task
def second_task(logger):
    logger.info("Second Task")


@task
def third_task(logger):
    logger.info("Third Task")


@flow
def first_flow():
    logger = get_run_logger()
    first_task(logger)
    second_task(logger)
    third_task(logger)


if __name__ == "__main__":
    first_flow()
