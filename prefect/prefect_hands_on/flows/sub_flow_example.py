from prefect import flow, task, get_run_logger


@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    return msg


@flow(name="Sub_flow")
def sub_flow(msg):
    logger = get_run_logger()
    logger.info(f"Sub_flow says: {msg}")


@flow(name="Hello Flow")
def sub_flow_example(name="world"):
    message = print_hello(name)
    sub_flow(message)


sub_flow_example("Marvin")
