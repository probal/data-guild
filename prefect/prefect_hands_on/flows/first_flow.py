from prefect import flow, task


@task
def first_task():
    print("First Task")


@flow
def first_flow():
    first_task()


if __name__ == "__main__":
    first_flow()
