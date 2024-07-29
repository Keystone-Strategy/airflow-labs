import os

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from configs import KsearchConfig

DAG_ID = os.path.basename(__file__).replace(".pyc", "").replace(".py", "")

with DAG(dag_id=DAG_ID, schedule="@daily", **KsearchConfig.KSEARCH_DAGS_DEFAULT_ARGS):
    EmptyOperator(task_id="task")
