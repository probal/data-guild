from prefect.artifacts import create_table_artifact
from prefect import flow


@flow
def artifact():
    highest_churn_possibility = [
        {'customer_id': '12345', 'name': 'John Smith', 'churn_probability': 0.85},
        {'customer_id': '56789', 'name': 'Jane Jones', 'churn_probability': 0.65}
    ]

    create_table_artifact(
        key="personalized-reach-out",
        table=highest_churn_possibility,
        description="# Shuvo, please reach out to these customers today!"
    )


if __name__ == "__main__":
    artifact()
