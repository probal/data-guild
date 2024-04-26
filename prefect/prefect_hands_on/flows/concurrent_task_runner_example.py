from prefect import flow, task, get_run_logger
from prefect.task_runners import ConcurrentTaskRunner
import time


@task
def task_1():
    logger = get_run_logger()
    logger.info("Task 1 is running")


@task
def task_2():
    logger = get_run_logger()
    logger.info("Task 2 is running")


@task
def task_3():
    logger = get_run_logger()
    logger.info("Task 3 is running")


@task
def task_4():
    logger = get_run_logger()
    logger.info("Task 4 is running")


@flow()
def concurrent_task_runner_example(task_runner_class=ConcurrentTaskRunner):
    logger = get_run_logger()
    logger.info("Running ConcurrentTaskRunner flow")
    task_1.submit()
    task_2.submit()
    task_3.submit()
    task_4.submit()


if __name__ == "__main__":
    concurrent_task_runner_example()
